
import streamlit as st
import pickle
import numpy as np


st.title("INDUSTRIAL COPPER MODELING")
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #061E42;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
   option=st.selectbox("SELECT ONE:",("REGRESSION","CLASSIFICATION"),index=None,placeholder=" ")


if option=="REGRESSION":
    with st.form("my-form"):
        status = ['Won', 'Lost', 'Draft', 'To be approved', 'Not lost for AM','Wonderful', 'Revised', 'Offered', 'Offerable']
        status_dict = {'Won':7, 'Draft':0, 'To be approved':5, 'Lost':1, 'Not lost for AM':2, 'Wonderful':8, 'Revised':6, 'Offered':4,
                        'Offerable':3}
        item_type = ['W', 'WI', 'S', 'PL', 'IPL', 'SLAWR', 'Others']
        item_type_dict = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}
        country = [ 25.,26.,27.,28.,30.,32.,38.,39.,40.,44.8930221,77.,78.,79.,80.,84.,89.,107.,113.]
        application = [10., 41., 15.,  4., 59., 38., 56., 42., 26., 27., 20., 66., 29.,28., 22., 40., 25., 67.,  3., 79., 99.,  2., 19.,  5., 39., 69.,70., 65., 58., 68.]
        product = [611728,611733,611993,628112,628117,628377,     640400,     640405,     640665,  164141591,
                    164336407,  164337175, 1282007633, 1332077137, 1665572032,1665572374, 1665584642, 1665584662, 1668701376, 1668701698,
                1668701718, 1668701725, 1670798778, 1671863738, 1671876026,1690738206, 1690738219, 1693867550, 1693867563, 1721130331,
                1722207579]
        col1, col2, col3 = st.columns([5, 1,5])
        with col1:
            st.write(' ')
            status = st.selectbox('Status', status,help='The "status" column likely describes the current status of the transaction or item. This information can be used to track the progress of orders or transactions, such as "Draft" or "Won."')
            item_type = st.selectbox('Item Type', item_type,help='This column categorizes the type or category of the items being sold or produced.')
            country = st.selectbox('Country',country,help=' The "country" column specifies the country associated with each customer. This information can be useful for understanding the geographic distribution of customers and may have implications for logistics and international sales.')
            application = st.selectbox('Application',application,help='The "application" column defines the specific use or application of the items. This information can help tailor marketing and product development efforts.')
            product_ref = st.selectbox('Product Reference', product,help=' The "product_ref" column seems to be a reference or identifier for the specific product. This information is useful for identifying and cataloging products in a standardized way.')
        with col3:
            st.write(' ')
            quantity_tons = st.slider('Enter Quantity Tons', 0.00001 ,1000000000.0,100.0,help='This column indicates the quantity of the item in tons, which is essential for inventory management and understanding the volume of products sold or produced.')
            thickness = st.slider('Enter thickness',0.18 ,2500.0,help='The "thickness" column provides details about the thickness of the items. It is critical when dealing with materials where thickness is a significant factor, such as metals or construction materials.')
            width = st.slider('Enter width',1,2990,help='The "width" column specifies the width of the items. It is important for understanding the size and dimensions of the products.')
            #customer = st.text_input('customer ID (Min:12458 to Max:2147483647)')
            ordertodelivery=st.slider('ordertodelivery_days',1.0,448.0,help='This column tells the how much time left between order time and delivery.')
            st.write(' ')
            st.write('  ')
            submit_bt = st.form_submit_button(label='Predict Selling Price')
            st.markdown('''
            ''', unsafe_allow_html=True)

        if submit_bt:
            with open(r'C:\Users\yaazhisai\Desktop\copper\ranforest_pkl', 'rb') as f:
                model = pickle.load(f)
            
            # make array for all user input values in required order for model prediction
            data = np.array([[ country, 
                                status_dict[status], 
                                item_type_dict[item_type], 
                                application, 
                                product_ref, 
                                np.log(float(quantity_tons)), 
                                np.log(float(thickness)),
                                np.log(float(width)),
                                ordertodelivery
                        ]])
            

            y_pred = model.predict(data)
            #inverse transformation 
            price_bfr = np.exp(y_pred[0])
            price_aft = np.round(price_bfr,2)

            st.write(f"THE PREDICTED SELLING PRICE IS:{price_aft}")


elif option=="CLASSIFICATION":
   with st.form("my_form1"):
        item_type = ['W', 'WI', 'S', 'PL', 'IPL', 'SLAWR', 'Others']
        item_type_dict = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}
        country = [ 25.,26.,27.,28.,30.,32.,38.,39.,40.,44.8930221,77.,78.,79.,80.,84.,89.,107.,113.]
        application = [10., 41., 15.,  4., 59., 38., 56., 42., 26., 27., 20., 66., 29.,28., 22., 40., 25., 67.,  3., 79., 99.,  2., 19.,  5., 39., 69.,70., 65., 58., 68.]
        product = [611728,611733,611993,628112,628117,628377,     640400,     640405,     640665,  164141591,
                    164336407,  164337175, 1282007633, 1332077137, 1665572032,1665572374, 1665584642, 1665584662, 1668701376, 1668701698,
                1668701718, 1668701725, 1670798778, 1671863738, 1671876026,1690738206, 1690738219, 1693867550, 1693867563, 1721130331,
                1722207579]
        col1,col2,col3 = st.columns([5,1,5])
        with col1:
            item_type = st.selectbox('Item Type', item_type,help='This column categorizes the type or category of the items being sold or produced.')
            country = st.selectbox('Country',country,help=' The "country" column specifies the country associated with each customer. This information can be useful for understanding the geographic distribution of customers and may have implications for logistics and international sales.')
            application = st.selectbox('Application',application,help='The "application" column defines the specific use or application of the items. This information can help tailor marketing and product development efforts.')
            product_ref = st.selectbox('Product Reference', product,help=' The "product_ref" column seems to be a reference or identifier for the specific product. This information is useful for identifying and cataloging products in a standardized way.')
            
        with col3:
            st.write(' ')
            quantity_tons = st.slider('Enter Quantity Tons',0.00001,1000000000.0,100.0,help='This column indicates the quantity of the item in tons, which is essential for inventory management and understanding the volume of products sold or produced.')
            selling_price = st.slider('Selling Price',0.1,100001000.0,help=' The "selling_price" column represents the price at which the items are sold. This is a critical factor for revenue generation and profitability analysis.')
            thickness = st.slider('Enter thickness',0.18,2500.0,help='The "thickness" column provides details about the thickness of the items. It is critical when dealing with materials where thickness is a significant factor, such as metals or construction materials.')
            width = st.slider('Enter width',1,2990,help='The "width" column specifies the width of the items. It is important for understanding the size and dimensions of the products.')
            #customer = st.text_input('customer ID (Min:12458 to Max:2147483647)')
            ordertodelivery=st.slider('ordertodelivery_days',1.0,448.0,help='This column tells the how much time left between order time and delivery.')
            st.write(' ')
            st.write('  ')
            submit_bt = st.form_submit_button(label='Predict Status')
            st.markdown('''
            ''', unsafe_allow_html=True)

        if submit_bt:
            with open(r'C:/Users/yaazhisai/Desktop/copper/etc1_pkl', 'rb') as f:
                model = pickle.load(f)

                          
                # make array for all user input values in required order for model prediction
                data = np.array([[ country, 
                                    item_type_dict[item_type], 
                                    application, 
                                    product_ref, 
                                    np.log(float(quantity_tons)),
                                    np.log(float(thickness)),
                                    np.log(float(width)),
                                    np.log(float(selling_price)),
                                    ordertodelivery
                            ]])
                

                y_pred= model.predict(data)
                st.write(y_pred[0])
                if y_pred[0]==1:
                    st.write(f"THE PREDICTED STATUS IS WON")
                else:
                    st.write(f"THE PREDICTED STATUS IS LOST")


            
