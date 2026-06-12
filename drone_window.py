from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QPointF, QPropertyAnimation, QTime
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, QBrush
from simulation.drone_sim import DroneSim

class DroneWindowReal(QWidget):
    def __init__(self, food_choice):
        super().__init__()
        self.setWindowTitle(f"Drone Delivery - {food_choice}")
        self.setGeometry(50, 50, 700, 650)
        self.food_choice = food_choice
        self.sim = DroneSim()

        self.map_bg = QPixmap("gps_map.png").scaled(700, 650)
        self.drone_pixmap = QPixmap("drone_real.png").scaled(40, 40)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_sim)
        self.timer.start(200)  # معدل أبطأ ليظهر الحركة

        self.label = QLabel(f"Delivering: {food_choice}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size:18px;font-weight:bold;color:#00aaff;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.current_pos = QPointF(self.sim.start[0]*30+10, self.sim.start[1]*30+10)
        self.anim = QPropertyAnimation(self, b"dummy")
        self.target_pos = self.current_pos

    def get_dummy(self): return 0
    def set_dummy(self, val): self.update()
    dummy = property(get_dummy, set_dummy)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.map_bg)

        # Obstacles
        for y in range(self.sim.GRID_SIZE):
            for x in range(self.sim.GRID_SIZE):
                if self.sim.grid[y][x] == 1:
                    painter.setBrush(QBrush(QColor(200,50,50,180)))
                    painter.drawRoundedRect(x*30+5, y*30+5, 25, 25, 5, 5)

        # Path
        if self.sim.path and self.sim.path_index>0:
            for i in range(self.sim.path_index-1):
                x1, y1 = self.sim.path[i]
                x2, y2 = self.sim.path[i+1]
                color = QColor(0, int(255*(i/len(self.sim.path))), 255)
                pen = QPen(color, 4, Qt.SolidLine, Qt.RoundCap)
                painter.setPen(pen)
                painter.drawLine(x1*30+25, y1*30+25, x2*30+25, y2*30+25)

        # Start & Goal
        painter.setBrush(QBrush(QColor(0,255,0)))
        sx, sy = self.sim.start
        painter.drawEllipse(sx*30+20, sy*30+20, 20, 20)

        painter.setBrush(QBrush(QColor(255,0,0)))
        gx, gy = self.sim.goal
        painter.drawEllipse(gx*30+20, gy*30+20, 20, 20)

        # Drone
        painter.drawPixmap(int(self.current_pos.x()), int(self.current_pos.y()), self.drone_pixmap)

    def update_sim(self):
        finished = self.sim.step()
        x, y = self.sim.drone_pos
        self.target_pos = QPointF(x*30+10, y*30+10)
        self.anim.stop()
        self.anim.setStartValue(self.current_pos)
        self.anim.setEndValue(self.target_pos)
        self.anim.setDuration(200)
        self.anim.start()
        self.current_pos = self.target_pos

        if finished:
            if not hasattr(self, "delivered"):
                self.delivered = True
                self.delivery_time = QTime.currentTime().toString("HH:mm:ss")
                self.label.setText(f"✅ Order {self.food_choice} delivered at {self.delivery_time}!")
                self.timer.stop()
                from gui.reorder_page import ReorderPage
                self.reorder_window = ReorderPage()
                self.reorder_window.show()
                self.close()
        else:
            current_time = QTime.currentTime().toString("HH:mm:ss")
            self.label.setText(f"🚁 Drone Pos: {self.sim.drone_pos} | Time: {current_time}")

        self.update()