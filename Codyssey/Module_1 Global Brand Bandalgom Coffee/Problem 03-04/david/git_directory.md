# 문제 04 - 보너스 과제

# 1. 버전 관리 시스템의 종류 3가지를 Markdown 문서로 제출한다.
(1) 로컬 버전 관리 시스템 [ Local VCS ]
- 각 파일의 변경 내역을 로컬에만 저장한다. => 내가 혼자 버전 관리를 하는 것이다.
- 다른 사람과 협업이 어렵고 백업이 불안정하다.

(2) 중앙 집중식 버전 관리 시스템 [ Centralized VCS ]
- 하나의 중앙 서버에서 모든 변경 이력을 관리한다.
- 협업이 가능하며 중앙 통제가 쉽다. (장점)
- 중앙 서버 장애 시 전체 작업 중단 위험이 있다. (단점)

(3) 분산 버전 관리 시스템 [ Distributed VCS ]
- 각 개발자가 전체 프로젝트 이력을 로컬에 복제하여 관리한다.
- 속도가 빠르고 분산 작업이 용이하다. (장점)


# 2. .git 디렉토리의 역할의 의미를 Markdown 문서로 제출한다.
.git 디렉토리는 Git 저장소의 핵심 디렉토리로, Git이 프로젝트의 버전 관리를 수행하는 데 필요한 모든 정보를 저장합니다.
만일 .git 폴더가 없으면 Git은 해당 디렉토리를 버전 관리 대상으로 인식하지 못한다.

[ 주요 역할 ]
(1) 버전 기록 저장 : 커밋된 모든 변경사항 정보를 저장한다
(2) 브랜치 정보 관리 : 현재 브랜치, HEAD 포인터 등의 참조 정보를 유지한다
(3) 스테이징 영역 : 커밋 전 임시 저장소 역할
(4) 설정 정보 보관 : 사용자 정보, 원격 저장소 URL, Git 동작 설정 등 ('config' 파일)
(5) hooks : 커밋 전후 자동 실행 스크립트 지정이 가능하다.


# 3. 작업 디렉토리에 .git디렉토리를 삭제한 후 git의 상태를 확인한다. 휴지통에서 .git디렉토리를 복원한 후 git의 상태를 확인한다.

# (1) 작업 디렉토리에서 .git디렉토리를 삭제 전 git 상태 확인
PS C:\Users\gram\AppData\Local\Programs\Python\Python39\david> ls -Force


    디렉터리: C:\Users\gram\AppData\Local\Programs\Python\Python39\david


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d--h--      2025-07-17   오후 1:01                .git
d-----      2025-07-16   오후 3:28                venv
-a----      2025-07-16   오후 3:14           2480 app.py
-a----      2025-07-16   오후 4:16           3860 calculator.py
-a----      2025-07-17   오후 1:00           1112 git_directory.md
-a----      2025-07-16   오후 7:29           1672 minmax_calculator.py


PS C:\Users\gram\AppData\Local\Programs\Python\Python39\david> git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py
        calculator.py
        git_directory.md
        minmax_calculator.py
        venv/

nothing added to commit but untracked files present (use "git add" to track)

# (2) 작업 디렉토리에서 .git디렉토리를 삭제 후 git 상태 확인
PS C:\Users\gram\AppData\Local\Programs\Python\Python39\david> git status
fatal: not a git repository (or any of the parent directories): .git

# (3) 휴지통에서 .git디렉토리를 복원한 후 git 상태 확인
PS C:\Users\gram\AppData\Local\Programs\Python\Python39\david> git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py
        calculator.py
        git_directory.md
        minmax_calculator.py
        venv/

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\gram\AppData\Local\Programs\Python\Python39\david>