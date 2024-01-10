![image](https://github.com/TAEHOONLIMKOREA/Practice_Flask_Vue/assets/87262811/bda548d3-36b4-4185-a400-808ce2fd7da3)
# 프로젝트 구성
- 먼저 프로젝트명으로 폴더를 만든 후 하위에 frontend와 backend 폴더 구성을 해주어야한다.<br/>
- frontend 폴더는 vue/cli를 이용하여 프로젝트를 생성해 줄 때 만들면 됨 <br/>
  (ex. vue create frontend) <br/>
- 이후 backend 폴더를 만들고 각 서비스 단의 세부 생성 과정은 아래 참고<br/>

### 폴더 구조 예시 사진 
![image](https://github.com/TAEHOONLIMKOREA/Practice_Flask_Vue/assets/87262811/8f4f5459-c9c4-4593-a33b-2bbb7731e9d8)
<hr/>

# backend

## python flask web framework

### vscode에서 python 실행환경 구성
#### 가상환경 설정
- 터미널 창 실행 <br/>
- python -m venv venv <br/>
#### 인터프리터 설정
- [ Ctrl + Shift + P ] 키를 눌러 ">select Interpreter"를 검색해서 선택 <br/>
![image](https://github.com/TAEHOONLIMKOREA/Practice_Flask_Vue/assets/87262811/e3dfa28f-9f1d-4016-9f08-4d36bd249900)

- 생성한 venv가상 환경 이름과 동일한 것을 선택 <br/>
![image](https://github.com/TAEHOONLIMKOREA/Practice_Flask_Vue/assets/87262811/c0d6be6e-3782-4cdf-9482-6a8106bbf731)

- 이후 기존에 열려있던 터미널 창을 닫고, 다시 터미널 창을 열어준다 (Ctrl + Shift + `)
![image](https://github.com/TAEHOONLIMKOREA/Practice_Flask_Vue/assets/87262811/a3df9935-ce23-48e2-ba1b-c6e50244f56f)

<hr/>

# frontend

###  vscode에서 vue 개발환경 구성:
Window 11<br/>
node.js 20.10.0 <br/>
- vue/cli 설치<br/>
(npm install -g @vue/cli) <br/>
(npm이 안되면 yarn 1.xx으로 대체 하여 설치, yarn 설치 방법은 Mac과 Window가 다르니 참고) <br/>

Visual Studio Code<br/>
- Extensions (Vetur, HTML CSS Support, vue 3 snippets)

#### 프로젝트 생성
```
vue create "프로젝트명" <br/>
```
#### 개발 서버 실행
```
npm run serve <br/>
```

#### Project setup
```
npm install
```

#### Compiles and minifies for production
```
npm run build
```

#### Lints and fixes files
```
npm run lint
```

<hr/>

# frontend와 backend 연동
- Flask와 Vue를 연동하는 방법은 2가지가 존재한다. 통합구축과 분리구축인데 일반적으로 분리구축이 규모가 커졌을 때 관리가 쉽다

## 통합구축 방법 (서버 1개)
- 기존의 vue 사용법 바로 npm run serve 명령어를 이용해 개발 서버를 실행시키는 것이 아님
- npm run build 명령어를 이용하여 vue형식의 파일을 html, js, css 파일로 변환 시켜서 flask에서 사용해야함


### Edit frontend/vue.config.js
![image](https://github.com/TAEHOONLIMKOREA/Practice_Flask_Vue/assets/87262811/c8102962-cb6b-4dcc-996e-bbe6001d8726)

### Frontend Build
- cd frontend<br/>
- npm run build<br/>

### Edit backend/main.py
![image](https://github.com/TAEHOONLIMKOREA/Practice_Flask_Vue/assets/87262811/8d4e36fd-968d-4f59-9dd9-1179cad347cc)

### Execute & Access
- cd backend<br/>
- python main.py<br/>

## 분리구축 방법 (서버 2개)
- 서버를 두 개를 띄워서 하나는 Frontend(Vue-Nodejs)에서 라우팅기능을 이용한 렌더링 기능을 사용하고 하나는 Backend(Flask)에서 RestAPI로 데이터만 주고받는다.
- 이렇게 구성할 경우 브라우저 정책(동일 출처 정책(Same-Origin Policy))에 따라 JavaScript코드가 다른 도메인의 리소스에서 접근하는 것을 막는데, 이 것을 허용해주는 것이 CORS다.
- CORS는 "Cross-Origin Resource Sharing"의 약자로 JavaScript 코드가 다른 도메인의 리소스에 접근하는 것을 허용하는 보안 메커니즘을 말함
- Flask 웹프레임워크에서 CORS를 다루려면, Flask-CORS 라이브러리를 사용해야함
- Flask-CORS 사용하여 Flask 서버에서 브라우저에게 어떤 도메인에서의 요청을 허용하게 설정 가능
- 이를 통해 AJAX, Jquery, fetch 등의 데이터 통신 요청을 허용하게 할수 있는데 본 프로젝트에서는 fetch()를 사용

### 1. FLASK CORS 설정
![Alt text](image.png)

### 2. 플러그인 설치
- Bootstrap
- Vue Router
- Vuex (아직은 필요 없어보이고 프로그램이 커지면 필요.. 추후 상황보고 설치하도록 하자..)

#### Bootstrap 설치
```
npm install bootstrap --save
```


<hr/>

## 기타 추가 사항
#### git
- vue를 통해 프로젝트를 생성하면 .git 폴더와 .gitignore파일이 forntend폴더 안에 만들어진다. 
- frontend폴더 안에 있는 .git폴더를 삭제하고 .gitignore파일을 상위 폴더(루트)로 옮긴다<br/>
- gitignore 에 (venv/, frontend/dist/) 를 추가한다<br/>
#### pip
- freeze 를 이용하여 패키지 저장목록을 만들어 놓는다
```
pip freeze > requirements.txt
```
- 설치할 때는 pip install -r requirements.txt 명령어를 이용하면 됨

#### ESLint 패키지 필요시 추가 (설치시 코드 작성 잘해야함...)
- npm install eslint eslint-plugin-vue --save-dev<br/>
- ESLint는 프론트엔드 코드 스타일을 관리 및 정적 프로그래밍 수행에 사용<br/>(개발 환경에서 코드 품질을 유지하고 향상시키기 위해 사용)<br/>

<hr/>

# 에러 해결

#### Bootstrap Vue 에러(디자인 라이브러리)
- Vue 프로젝트에 Bootstrap 적용을 위해 아래와 같이 BootstrapVue를 적용하고 실행하니 에러 발생 <br/>
- https://bootstrap-vue.org/docs 홈페이지에서 다운로드 방법 확인<br/>

- With npm
```
npm install vue bootstrap bootstrap-vue
```
-  With yarn
```
yarn add vue bootstrap bootstrap-vue
```
<br/>

- main.js에 코드 추가 후 빌드 하면 에러 발생
![Alt text](image-2.png)

#### 결론 :  bootstrapVue는 Vue3는 지원하지 않는다! (제길..)
#### 해결 방안 : public/index.html파일에 bootstrap CSS와 JS를 직접 임포트

#### 꼭 bootstrap만 설치해야함 (bootstrap-vue X)
```
npm install bootstrap --save
```
- 이후 자세한 부트스트랩 적용 방법은 위 프론트엔드 부분 참고
