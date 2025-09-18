sudo apt-get update
sudo apt-get install -y python3-pip
pip3 install dynamixel-sdk

# 간단 테스트 스크립트 받기
cat > dxl_quick_test.py << 'EOF'
from dynamixel_sdk import *  # pip3 install dynamixel-sdk
PORT='/dev/ttyUSB0'; BAUD=57600; PROTOCOL=2.0; ID=1
ADDR_TORQUE_ENABLE = 64
ADDR_GOAL_POSITION = 116
ADDR_PRESENT_POSITION = 132
port = PortHandler(PORT)
packet = PacketHandler(PROTOCOL)
assert port.openPort(), "포트 오픈 실패"
assert port.setBaudRate(BAUD), "보레이트 설정 실패"
# 토크 ON
packet.write1ByteTxRx(port, ID, ADDR_TORQUE_ENABLE, 1)
# 중앙 근처로 이동(약 2048이 중앙)
packet.write4ByteTxRx(port, ID, ADDR_GOAL_POSITION, 2048)
# 현재 위치 읽기
pos, _, _ = packet.read4ByteTxRx(port, ID, ADDR_PRESENT_POSITION)
print("Present Position:", pos)
port.closePort()
EOF

python3 dxl_quick_test.py
