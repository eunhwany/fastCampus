# 1-04. 개발자 도구 사용하기

크롬 개발자도구를 보겠습니다.

접근하는 방법으로는, 메뉴 바에서 개발자 도구를 선택해 활성화하거나, 해당 요소를 클릭해서 선택할 수 있습니다.

개발자 도구에서는 여러 가지 작업을 수행할 수 있습니다.

먼저, Element 탭에서는 HTML 요소에 대해 조사하고, CSS를 확인하며 변경할 수 있습니다. 주로 화면에 보이는 내용을 확인하고 편집할 때 사용됩니다. Console 탭에 자바스크립트를 실행할 수도 있습니다.

우리가 오늘 확인할 부분은 네트워크 탭입니다. 네트워크 탭은 페이지를 로딩하는 데 필요한 네트워크 작업에 대한 결과를 시간 순으로 표시합니다. 이를 통해 웹서버와 주고받는 데이터의 실제 모습을 볼 수 있습니다.

특정 항목을 선택해서 해당 항목이 어떻게 요청되었고, 어떤 응답을 받았는지를 확인해 보겠습니다. 네이버 뉴스를 들어가 보겠습니다. 이 페이지를 로딩하면서 발생한 네트워크 요소가 모두 나옵니다.

가장 먼저 HTML 문서가 들어 있는 도큐먼트가 불러와지고, 그 다음에는 해당 문서에 스타일링을 하는 CSS가 들어있는 스타일시트가 불러와 집니다. 이후 자바스크립트와 사진 파일, 일반 텍스트 등이 로딩되는 것을 확인할 수 있습니다.

뉴스를 가져오는 데 사용한 HTTP 요청은 모두 GET이고요. 모두 정상적으로 불러와진 덕분에 200 상태코드를 확인할 수 있습니다.

이 중에서 가장 위에 있는 document 타입을 눌러보면 헤더가 나옵니다.

Headers 탭에는 HTTP가 요청하고 응답받아온 기초 정보가 들어 있습니다. General 과 request, response로 나뉘어져 있습니다. 서버의 도메인 네임, 사용 중인 브라우저, 날짜, 형식 등의 정보가 있습니다. 실제로 받아온 HTML 문서 데이터는 Response 탭에 있습니다.

개발자도구를 통해 웹 브라우저와 웹 서버 간에 어떤 HTTP 요청이 오가며 실제 어떤 데이터를 가지고 준비하는지를 확인해 보았습니다. 앞으로 개발자 도구를 더 많이 사용해볼 수 있을 것입니다.

크롬 개발자도구에 대한 정보는 구글 사이트에서 더 많이 얻을 수 있습니다. [https://developers.google.com/web/tools/chrome-devtools/](https://developers.google.com/web/tools/chrome-devtools/)