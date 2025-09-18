from dynamixel_sdk import *  # pip3 install dynamixel-sdk

PORT = '/dev/ttyUSB0'
BAUD = 57600
PROTOCOL = 2.0
ID = 1

ADDR_TORQUE_ENABLE = 64
ADDR_GOAL_POSITION = 116
ADDR_PRESENT_POSITION = 132

port = PortHandler(PORT)
packet = PacketHandler(PROTOCOL)

if not port.openPort():
    print("포트 오픈 실패")
    quit()

if not port.setBaudRate(BAUD):
    print("보레이트 설정 실패")
    quit()

# 토크 ON
packet.write1ByteTxRx(port, ID, ADDR_TORQUE_ENABLE, 1)

# 목표 위치 (약 2048이 중앙)
packet.write4ByteTxRx(port, ID, ADDR_GOAL_POSITION, 2048)

# 현재 위치 읽기
pos, _, _ = packet.read4ByteTxRx(port, ID, ADDR_PRESENT_POSITION)
print("Present Position:", pos)

port.closePort()
