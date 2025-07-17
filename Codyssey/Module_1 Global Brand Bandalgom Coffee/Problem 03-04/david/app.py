"""
이 코드는 음성 출력 웹 애플리케이션이다.
컴퓨터에 Flask라는 도구와 gTTS라는 도구를 설치해서 만든 간단한 웹사이트이다.
이 웹사이트는 사용자가 접속하면 "Hello, DevOps"라는 문장을 음성으로 바꿔서 들려준다.

"""


# Flask, HTTP 요청 처리, 응답 생성을 위한 모듈 불러오기
# Flask : 웹사이트를 만들 수 있게 도와주는 도구이다.
# 웹페이지 요청이 오면 어떻게 응답할지 정할 수 있다.
from flask import Flask, request, Response

# 운영 체제 환경변수 접근을 위한 모듈
# os : 컴퓨터 환경 설정 정보를 가져올 수 있게 해주는 도구
import os

# 메모리 버퍼를 위한 모듈 (파일처럼 다룰 수 있음)
# BytesIO : mp3 파일을 진짜 파일처럼 메모리에 저장할 수 있게 해주는 도구
from io import BytesIO

# gTTS(Google Text-to-Speech) 패키지 : 텍스트를 음성으로 변환하는 기능 제공
from gtts import gTTS

# 웹사이트가 기본으로 어떤 언어로 만들지 정한다.
# 환경 변수에서 'DEFAULT_LANG' 값을 가져오고, 없으면 기본값으로 'ko'(한국어)를 사용
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')

# Flask 애플리케이션 객체 생성
app = Flask(__name__)

# 루트 경로("/")에 접근했을 때 실행될 함수 정의
@app.route("/")
def home():

    # 클라이언트에서 들려줄 텍스트
    text = "Hello, DevOps"

    # 사용자가 URL에 lang 파라미터를 주면 그 값을 사용, 없으면 DEFAULT_LANG 사용
    lang = request.args.get('lang', DEFAULT_LANG)

    # 음성 데이터를 저장할 메모리 버퍼(파일처럼 사용 가능)를 생성
    fp = BytesIO()

    # gTTS로 text를 음성으로 변환해서 fp 버퍼에 저장
    gTTS(text, "com", lang).write_to_fp(fp)

    # fp에 저장된 mp3 데이터를 HTTP 응답으로 변환
    # imetype='audio/mpeg; => 브라우저가 mp3로 인식하게 함
    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

# 이 파일이 직접 실행될 때만 아래 코드 실행 (import된 경우 실행 X)
if __name__ == '__main__':

    # 웹 서버 실행
    # 0.0.0.0 => 외부에서도 접속 가능하도록 모든 IP에 바인딩
    # 80 => 웹사이트가 보통 사용하는 기본 포트 번호 (http://주소 로 접속 가능)
    app.run('0.0.0.0', 80)