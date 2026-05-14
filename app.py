#%%
import streamlit as st
import pickle

with open("linear_model.pkl","rb") as f:
    model=pickle.load(f)

    st.title("jitne hours padoge utne number laoge")
    st.header("lets try something new!")
    st.write("abb sab chota likhega yeh")

    hours=st.number_input("please enter your number of hours:")
    bt=st.button("click Here ✅")
    output=model.predict([[hours]])[0]
    # output=str(output)
 
if bt:
    if hours<0 or hours>24:
        st.error("please enter a valid hour")
    elif 0<hours<9.50:
        if output<33:
            output=str(output)
            st.warning(f"sorry tum fail hone me success ho gay-marks:{output[:5]}")
        else:
            output=str(output)
            st.info(f"you will get:{output[:5]}: you are pass")
    elif hours==0:
        st.error("padai karna suru kro ")
        
    else:
        st.success("you will get 100 marks ,welldone you are pass")


# %%
