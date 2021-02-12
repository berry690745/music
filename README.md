## Music
[제작자 유튜브](https://www.youtube.com/channel/UCv1unZDLpiO6c_7cBte7ZrA)

## 동작 시 주의사항
실행 시 파일을 IDE로 실행하지 마세요, 외부 오류가 발생할 수 있습니다.

혹은 해당에 파일을 IDE로 돌려야 한다면 FFMPEG을 IDE 프로젝트 안에서 빌드하세요.

## 버전
해당에 소스는 Python 버전 3.7.3을 권장합니다 (섹시베이비님 파이썬 버전 기준)

개발자 테스트 일때 Python 3.8.1 버전으로도 안정하게 돌아갑니다.

그 이하(이상)에 버전에서 작동은 보장해드릴 수 없습니다.

## 설치 모듈
해당에 파일은 설치 모듈이 필요합니다.

다음에 설치 모듈은 아래와 같습니다.

```
discord.py
discord.py[voice]
youtube_dl
```

만약 해당에 파일 중 설치되지 않은 게 있다면 설치해주세요

## 오류 발생

> No such file or directory

해당에 오류가 발생할 경우 내장 되어있는 `file`이 삭제되어있는 지 확인주세요.

혹은 해당에 파일의 지정된 위치가 바뀌었는지 확인해주세요.

> ffmpeg was not found

해당에 오류가 발생할 경우 본인이 ffmpeg을 빌드하지 않을 가능성이 있습니다.

혹은 해당에 ffmpeg을 환경 변수에 설정하지 않았거나 ide로 실행했을 가능성이 있습니다.

## 왜 IDE는 안되나요?
해당에서 IDE는 ffmpeg 자체을 빌드하지 않았기 때문에 `IDE` 콘솔에 ffmpeg을 쳐도 동작이 안됩니다.

그러나 이는 ffmpeg was not found가 떻을 때 이야기 입니다.

하지만 오류가 나지 않는 다면 ide로 실행하여도 상관은 없습니다.
