from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime
import csv
import os # [필수] 파일 검사를 위해 추가

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def show_form(request: Request) :
    return templates.TemplateResponse(
        "joinus.html", {"request": request}
    )

@app.post("/join")
def submit_form(
    request: Request,
    name: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    age: str = Form(...),
    gender: str = Form(...)
) :
    print(">>>> [POST - /join]", name, address, phone, email, age, gender)
    
    # 1. 파일 경로 설정
    csv_file = "person.csv"
    
    # 2. 파일이 존재하는지 미리 확인 (이게 훨씬 안전해요!)
    file_exists = os.path.exists(csv_file)

    # 3. 파일 열기 (a: 이어쓰기, encoding='utf-8-sig': 엑셀에서 한글 안 깨지게)
    # 팁: utf-8 대신 'utf-8-sig'를 쓰면 엑셀에서 한글이 더 잘 보입니다.
    with open(csv_file, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        # 4. 파일이 없으면 제목(Header) 한 줄 쓰기
        if not file_exists:
            writer.writerow(["가입일시", "이름", "주소", "전화번호", "이메일", "나이", "성별"])
        
        # 5. 진짜 날짜 구하기
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 6. 데이터 쓰기 (변수 now를 넣어야 시간이 찍힙니다)
        writer.writerow([now, name, address, phone, email, age, gender])
    
    # return {
    #     "name": name, 
    #     "address": address, 
    #     "phone": phone,  
    #     "email": email, 
    #     "age": age, 
    #     "gender": gender
    # }
    
    # return templates.TemplateResponse("")
    
    # return HTMLResponse(f"""
    #     <!DOCTYPE html>
    #     <html>
    #         <body>
    #             <h1>결과 페이지</h1>
    #             <ul>
    #                 <li>성명: {name}</li>
    #                 <li>주소: {address}</li>
    #                 <li>이메일: {email}</li>
    #             <ul>
    #         </body>
    #     </html>
    # """)
    
    return templates.TemplateResponse(
        "result.html", {
        "request": request,
        "name": name, 
        "address": address, 
        "phone": phone,  
        "email": email, 
        "age": age, 
        "gender": gender
    })