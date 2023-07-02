import streamlit as st

from whatsapp_api_client_python import API

greenAPI = API.GreenApi("7103836596", "0330f6de316f4597a900bb8263269670c009b42cd7d947709e")
st.title("Enquiry Form")
st.subheader("Fill the below details")
with st.form("email_form",clear_on_submit=True):
    name=st.text_input("Your Name")
    email=st.text_input("Your Email Address")
    phone=st.text_input("your Phone Number")
    excel=st.checkbox("Excel")
    sql=st.checkbox("SQL")
    vba=st.checkbox("VBA")
    msgbox=st.text_input("Comments")
    submitbutton=st.form_submit_button("Submit")

ph=str(phone)+"@c.us"

def course():
    if excel==True:
        ex="excel"
        return ex
    elif sql==True:
        ex="SQL"
        return ex
    elif vba==True:
        ex="VBA"
        return ex
c=course()
cc=str(c)
msg="Hey, I am " + name + ", my phone number is " + str(phone) + ", Email is " + email + " and i am interested in " + cc

if submitbutton:
    l=[msg]
    print(l)
    def main():
        response = greenAPI.sending.sendMessage(ph, msg)

        print(response.data)

    if __name__ == '__main__':
        main()






