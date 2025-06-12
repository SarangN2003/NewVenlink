#Original File
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VendorActionLocators:
    def __init__(self, driver):
        self.driver = driver

    EDIT = (By.XPATH, "//div[@class='hidden lg:block']//li[@title='Edit'][normalize-space()='Edit']")
    APPROVE = (By.XPATH, "//li[normalize-space()='Approve']")

    # def getEdit(self):
    #     return self.driver.find_element(*VendorActionLocators.EDIT)
    def getEdit(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            return wait.until(EC.presence_of_element_located(self.EDIT))
        except Exception as e:
            print(f"Edit button not found: {e}")
            raise

    # def getApprove(self):
    #     return self.driver.find_element(*VendorActionLocators.APPROVE)
    def getApprove(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            return wait.until(EC.presence_of_element_located(self.APPROVE))
        except Exception as e:
            print(f"Approve button not found: {e}")
            raise


class HomePage1:
    def __init__(self,driver):
        self.driver = driver

    # Cudtomer login page
    Email = (By.XPATH, "//input[@name='username']")
    Password = (By.XPATH, "//input[@name='password']")
    CheckBox = (By.XPATH, "//input[@name='termsConditionsCheckBox']")
    sign_in_button = SignIn = (By.XPATH, "//button[text()='SIGN IN']")

    # vendor request Login first Page
    click =(By.XPATH,"//div/div[text()='Vendor']")
    Name = (By.XPATH,"//input[@name='accountName']")
    vender_Type = (By.XPATH,"//button[@id='combobox-button-31']")
    vender_Typeselect = (By.XPATH,"//lightning-base-combobox-item[@id='combobox-button-31-1-31']")
    BusinessCase = (By.XPATH,"//div/textarea[@name='businessCase']")
    FirstName = (By.XPATH,"//input[@name='firstName']")
    LastName = (By.XPATH,"//input[@name='lastName']")
    Email2= (By.XPATH,"//input[@name='email']")
    Phone = (By.XPATH,"//input[@name='phone']")
    Next = (By.XPATH,"//div/button[text()='Next']")

    # vendor request Login Second Page
    #For Dev3
    TypeAService = (By.XPATH, "//input[@placeholder='Type a Service']")
    Services = (By.XPATH, "//span[@class='slds-listbox__option-text slds-listbox__option-text_entity']")

    TypeALocation = (By.XPATH, "//input[@placeholder='Type a Location']")
    Locations = (By.XPATH,"//span[@class='slds-listbox__option-text slds-listbox__option-text_entity']")
    Next2 = (By.XPATH, "//div/button[text()='Next']")


    #For Staging
    # TypeAService = (By.XPATH, "//input[@placeholder='Type a Service']")
    # Services = (By.XPATH,"//mark[normalize-space()='Corrosion Inhibitors']")
    #
    # TypeALocation = (By.XPATH, "//input[@placeholder='Type a Location']")
    # Locations = (By.XPATH,"//body/webruntime-app/lwr-router-container/webruntime-inner-app/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/c-theme-layout/div[@class='grid lg:grid-cols-12']/div[@class='lg:col-span-10 flex flex-col min-h-screen']/section[@class='flex-grow']/slot/webruntime-router-container/dxp_data_provider-user-data-provider/dxp_data_provider-data-proxy/community_layout-slds-flexible-layout[@class='lwc-2b5a72ratvd-host']/div[@class='lwc-2b5a72ratvd content-container']/community_layout-section[@class='comm-section-container lwc-6j9an5vbrcd-host']/div[@class='lwc-6j9an5vbrcd columns-content']/community_layout-column[@class='col-size_12-of-12 col-large-size_12-of-12 lwc-48aostf02bd-host']/div[@class='lwc-48aostf02bd column-content']/c-cust_vendor-list/div[@id='default-modal-21']/div[@class='bg-white rounded-lg shadow-lg max-w-4xl w-full h-72']/c-cust_vendor-request-form/div/div[@class='px-4 lg:h-74']/div[@class='flex flex-col gap-1']/div[@class='h-40']/div/div[@class='grid gap-2']/c-reusable-lookup[@class='location-input-lookup']/div[@class='slds-form-element m-0']/div[@class='slds-form-element__control']/div[@id='listbox-id-4-70']/ul[@role='presentation']/li[2]/div[1]/span[1]/span[1]")
    # Next2 = (By.XPATH, "//div/button[text()='Next']")

    # vendor request Login Third Page

    Radio1 = (By.XPATH,"(//span[@class='slds-radio_faux'])[2]")
    Radio2 = (By.XPATH, "(//span[@class='slds-radio_faux'])[4]")
    Radio3 = (By.XPATH, "(//span[@class='slds-radio_faux'])[6]")
    Radio4 = (By.XPATH, "(//span[@class='slds-radio_faux'])[8]")
    SelectAnOption = (By.XPATH,"(//button[@role='combobox'])")
    SelectAnOptionDropdown = (By.XPATH,"//lightning-base-combobox-item[@data-value='No']")
    Save = (By.XPATH,"(//button[normalize-space()='Save'])[1]")


###New Vendor Created
    Action = (By.XPATH,"//span[normalize-space()='Actions']")
    Action2 = (By.XPATH, "//span[normalize-space()='Actions']")

###Edit/About/Account Information####
    Legal_Entity_Name = (By.XPATH,"(//div[@type='text'])[2]")
    Parent_Account = (By.XPATH,"(//div[@type='search'])[1]")
    Parent_Account_click = (By.XPATH,"//mark[normalize-space()='Howard Campbell']")
    Phone_No = (By.XPATH,"(//div[@type='tel'])[1]")
    Website = (By.XPATH, "(//div[@type='text'])[3]")
    Client_Vendor_ID = (By.XPATH,"(//div[@type='text'])[4]")
    Account_Information = (By.XPATH,"(//button[@class='border rounded-lg gap-2 px-2 py-2 bg-blue-900 mr-2'])[1]")

    # custoner login page
    def getEmail(self):
        return self.driver.find_element(*HomePage1.Email)

    def getPassword(self):
        return self.driver.find_element(*HomePage1.Password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage1.CheckBox)

    def getSignIn(self):
        return self.driver.find_element(*HomePage1.SignIn)

# first Login Page
    def getclick(self):
        return self.driver.find_element(*HomePage1.click)

    def getName(self):
        return self.driver.find_element(*HomePage1.Name)

    def getvendertype(self):
        return self.driver.find_element(*HomePage1.vender_Type)

    def getvendertypeselect(self):
        return self.driver.find_element(*HomePage1.vender_Typeselect)

    def getBusinessCase(self):
        return self.driver.find_element(*HomePage1.BusinessCase)

    def getFirstName(self):
        return self.driver.find_element(*HomePage1.FirstName)

    def getLastName(self):
        return self.driver.find_element(*HomePage1.LastName)

    def getEmail2(self):
        return self.driver.find_element(*HomePage1.Email2)

    def getPhone(self):
        return self.driver.find_element(*HomePage1.Phone)

    def getNext(self):
        return self.driver.find_element(*HomePage1.Next)


#Second Login Page
    def getTypeAService(self):
        return self.driver.find_element(*HomePage1.TypeAService)

    def getServices(self):
        return self.driver.find_element(*HomePage1.Services)

    def getTypeALocation(self):
        return self.driver.find_element(*HomePage1.TypeALocation)

    def getLocations(self):
        return self.driver.find_element(*HomePage1.Locations)

    def getNext2(self):
        return self.driver.find_element(*HomePage1.Next2)

#Third Login Page

    def getRadio1(self):
        return self.driver.find_element(*HomePage1.Radio1)

    def getRadio2(self):
        return self.driver.find_element(*HomePage1.Radio2)

    def getRadio3(self):
        return self.driver.find_element(*HomePage1.Radio3)

    def getRadio4(self):
        return self.driver.find_element(*HomePage1.Radio4)

    def getSelectAnOption(self):
        return self.driver.find_element(*HomePage1.SelectAnOption)

    def getSelectAnOptionDropdown(self):
        return self.driver.find_element(*HomePage1.SelectAnOptionDropdown)

    def getSave(self):
        return self.driver.find_element(*HomePage1.Save)

#####New Vendor

    def getAction(self):
        return self.driver.find_element(*HomePage1.Action)


    def getAction2(self):
        return self.driver.find_element(*HomePage1.Action2)

###Edit/About/Account Information####

    def getLegal_Entity_Name(self):
        return self.driver.find_element(*HomePage1.Legal_Entity_Name)

    def getParent_Account(self):
        return self.driver.find_element(*HomePage1.Parent_Account)

    def getParent_Account_click(self):
        return self.driver.find_element(*HomePage1.Parent_Account_click)

    def getPhone_No(self):
        return self.driver.find_element(*HomePage1.Phone_No)

    def getWebsite(self):
        return self.driver.find_element(*HomePage1.Website)

    def getClient_Vendor_ID(self):
        return self.driver.find_element(*HomePage1.Client_Vendor_ID)

    def getAccount_Information(self):
        return self.driver.find_element(*HomePage1.Account_Information)


