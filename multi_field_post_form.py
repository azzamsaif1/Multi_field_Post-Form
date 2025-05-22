# import socket 

# HOST = '127.0.0.1'
# PORT = 1414

# # create server 
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(1)

# print(f"[Server Running] Visit: http://{HOST}:{PORT}")


# while True:
#     client_conn, client_addr = server_socket.accept()
#     request = client_conn.recv(1024).decode()
#     print("[Request Received]:\n", request)
    
#     #analysis request
    
#     request_line=request.splitlines()[0]
#     print(f"[First line from request]:>>> {request_line}")
#     method,path,_=request_line.split()
#     print(f"the method is {method} , path{path } , _{_}")
#     name=age=email=""
#     if method =="POST":
#         body=request.split("\r\n\r\n",1)[1]
#         print(f"[POST BODY] {body}")
#         fields=body.split("&")
#         print(f"[this is the fields ] >> {fields}")
#         for field in fields :
#             key,value=field.split("=")
#             print(f"Key = {key} , value ={value}")
            
#             if key=="name":
#                 name =value
#             elif key== "age":
#                 age=value
#             elif key=="email":
#                 email =value
#     if name or age or email :
#         message =f"<h2> Hello {name}!</h2><p>age :{age} </p> <p> Email:{email}</p>"
#     else:
#         message=""
#     html=f"""
#             <html>
#             <head> 
#                 <title>Multi Field Form </title>
#             </head> 
#                 <body> 
#                 <h1> fill the form </h1>
#                 <form method="POST" action="/">
#                     <input type="text" name="name" placeholder="Enter your name "><br>
#                     <input type="age" name="age" placeholder="Enter your age "><br>
#                     <input type="email" name="email" placeholder="Enter your email "><br>
#                     <button type="submit" > submit</button>
#                 </form>
#                 {message}
#                 </body> 
#             </html>
            
#     """
#     response=f"""
#                 HTTP/1.1 200 OK
#                 content-Type:text/html
#                 content-length:{len(html)}
                
# {html}
    
# """

#     client_conn.sendall(response.encode())
#     client_conn.close()

##Filer Code 


import socket

HOST = '127.0.0.1'
PORT = 8081

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Server Running] Visit: http://{HOST}:{PORT}")

while True:
    client_conn, client_addr = server_socket.accept()
    request = client_conn.recv(1024).decode()
    print("[Request Received]:\n", request)

    #analysis request :
    
    request_line = request.splitlines()[0]
    method, path, _ = request_line.split()

    name, age, email = "", "", ""

    if method == "POST":
        body = request.split("\r\n\r\n", 1)[1]
        print("[POST Body]:", body)

        #  >>>>>>
        fields = body.split("&")
        for field in fields:
            key, value = field.split("=")
            value = value.replace("+", " ")
            if key == "name":
                name = value
            elif key == "age":
                age = value
            elif key == "email":
                email = value

    # 
    if name and age and email:
        message = f"<h2>Hello {name}, age {age}, email: {email}</h2>"
    else:
        message = ""

    html = f"""
    <html>
        <head><title>Multi Field Form</title></head>
        <body>
            <h1>Submit Your Info</h1>
            <form method="POST" action="/">
                <input type="text" name="name" placeholder="Name"><br>
                <input type="text" name="age" placeholder="Age"><br>
                <input type="email" name="email" placeholder="Email"><br>
                <button type="submit">Submit</button>
            </form>
            {message}
        </body>
    </html>
    """

    response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html)}

{html}
"""
    client_conn.sendall(response.encode())
    client_conn.close()
