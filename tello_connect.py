#텔로와 컴퓨터를 연결한다
import socket
import cv2
import numpy as np

#텔로와 컴퓨터 간의 통신을 도와줄 소켓 생성
local_ip = '' #빈 문자열을 local_ip에 저장
local_port = 8889 #8889를 local_port에 저장/8889 : 컴퓨터가 텔로와 통신을 할 때 도와줄 UDP 포트번호
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #텔로와 통신을 가능하게 도와주는 소켓 생성 후 기능을 socket에 저장
                                                        #socket.AF_INET : 클라이언트와 서버가 다른 기기/socket.SOCK_DGRAM : UDP 방식
socket.bind((local_ip, local_port)) #소켓과 host 컴퓨터의 port 연결

#텔로의 ip와 port를 튜플로 저장
tello_ip = '192.168.10.1' #'192.168.10.1' : 텔로의 ip번호/텔로의 ip번호를 tello_ip에 저장
tello_port = 8889 #텔로가 컴퓨터와 통신을 할 때 도와줄 UDP 포트번호
tello_address = (tello_ip, tello_port) #텔로의 정보를 tello_adderss에 튜플 형식으로 저장

stream_state = True

#텔로에게 명령어를 보내는 함수
def send_command(command):
    socket.sendto(command.encode('utf-8'), tello_address)

send_command('command')
send_command('streamon')

#텔로로부터 영상을 받아온다
tello_video = cv2.VideoCapture('udp://'+tello_ip+':11111')

# 텔로 실행 코드
while stream_state:

    # 텔로의 영상 정보를 받아옴
    state, img = tello_video.read() # state : 영상 상태 값을 t or f로 반환 / img : 영상의 이미지를 받아옴

    # 텔로영상을 보여주는 창 생성
    cv2.imshow("tello", img)

    # fps값 설정 후 특정값(q)를 누를시 while문 탈출
    if cv2.waitKey(1) == ord('q'): break

# 텔로 영상값을 반환
tello_video.release()

# 텔로영상을 보여주는 창 닫기
cv2.destroyWindow('tello')

# 텔로 스트림모드 종료
send_command('streamoff')