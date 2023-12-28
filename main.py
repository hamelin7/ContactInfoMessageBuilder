import csv
def getDataInput():
    lContactData = []

    with open('contactlist.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            lContactData.append(row)
    return lContactData

def contactTypeList(lContactData):
    lContactTypes = {}
    for contact in lContactData:
        lContactTypes[contact[0], contact[1]] = [contact[7], contact[14], contact[15], contact[16], contact[17], contact[18], contact[19]]
    return lContactTypes

def remoteAuthList(lContactData):
    lRemoteAuth = {}
    for contact in lContactData:
        lRemoteAuth[contact[0], contact[1]] = [contact[15]]
    return lRemoteAuth

def remoteAuth(lRemoteAuth):
    message = ""
    remoteSupport = []

    for key, value in lRemoteAuth.items():
        if "Yes" in value[0]:
            remoteSupport.append(" ".join(key))
            message = f"Are there any employees who are not authorized to request remote support? {', '.join(remoteSupport)}"
    print(message)

def onsiteAuthList(lContactData):
    lOnsiteAuth = {}
    for contact in lContactData:
        lOnsiteAuth[contact[0], contact[1]] = [contact[16]]
    return lOnsiteAuth

def onsiteAuth(lContactTypes):
    message = ""
    onsiteSupport = []

    for key, value in lContactTypes.items():
        if "Yes" in value[0]:
            onsiteSupport.append(" ".join(key))
            message = f"Are there any employees who are not authorized to request onsite support? {', '.join(onsiteSupport)}"
    print(message)

def emergencyAuthList(lContactData):
    lEmergencyAuth = {}
    for contact in lContactData:
        lEmergencyAuth[contact[0], contact[1]] = [contact[17]]
    return lEmergencyAuth

def emergencyAuth(lContactTypes):
    message = ""
    emergencySupport = []

    for key, value in lContactTypes.items():
        if "Yes" in value[0]:
            emergencySupport.append(" ".join(key))
            message = f"Are there any employees who are not authorized to request emergency support? {', '.join(emergencySupport)}"
    print(message)

def nonIncludedAuthList(lContactData):
    lNonIncludedAuth = {}
    for contact in lContactData:
        lNonIncludedAuth[contact[0], contact[1]] = [contact[19]]
    return lNonIncludedAuth

def nonIncludedAuth(lContactTypes):
    message = ""
    nonIncludedSupport = []

    for key, value in lContactTypes.items():
        if "Yes" in value[0]:
            nonIncludedSupport.append(" ".join(key))
            message = f"Are there any employees who are not authorized to request 'non-included' services? {', '.join(nonIncludedSupport)}"
    print(message)

def securityAuthList(lContactData):
    lSecurityAuth = {}
    for contact in lContactData:
        lSecurityAuth[contact[0], contact[1]] = [contact[18]]
    return lSecurityAuth

def securityAuth(lContactTypes):
    message = ""
    securitySupport = []

    for key, value in lContactTypes.items():
        if "Yes - All Users" in value[0] or "Yes - Except Secure Users" in value[0]:
            securitySupport.append(" ".join(key))
            message = f"Who is authorized to request Paragus change permissions on folders, grant access to another user's data, or grant access to another user's email? {', '.join(securitySupport)}"
    print(message)

def spendingLimitList(lContactData):
    lSpendingLimit = {}
    for contact in lContactData:
        lSpendingLimit[", ".join([contact[0], contact[1]])] = [contact[14]]
    #print(lSpendingLimit)
    return lSpendingLimit

def spendingLimit(lContactTypes):
    message = ""
    spendingLimit = []

    for key, value in lContactTypes.items():
        if "$250" in value[0] or "$500" in value[0] or "$1000" in value[0] or "$1500" in value[0] or "$2500" in value[0] or "$5000" in value[0] or "$10000" in value[0] or "$25000" in value[0] or "$50000" in value[0] or "No Limit" in value[0]:
            spendingLimit.append(f"{key}: {value[0]}")
    message = f"Who is authorized to spend more than the company default spending limit? {', '.join(spendingLimit)}"
    print(message)

def secureUsersList(lContactData):
    lSecureUsers = {}
    for contact in lContactData:
        lSecureUsers[contact[0], contact[1]] = [contact[18]]
    return lSecureUsers

def secureUsers(lContactTypes):
    message = ""
    secureUsers = []

    for key, value in lContactTypes.items():
        if "Yes - Except Secure Users" in value[0]:
            secureUsers.append(" ".join(key))
            message = f"Are there any users whose data they are not authorized to request access to (i.e. owner, CFO, HR)? Yes{', '.join(secureUsers)}"
        elif "Yes - All Users" in value[0]:
            message = "Are there any users whose data they are not authorized to request access to (i.e. owner, CFO, HR)? No"
    print(message)

def pocTypes(lContactTypes):
    message = ""
    ppoc1 = None
    ppoc2 = None
    ppoc3 = None
    epoc1 = None
    epoc2 = None
    epoc3 = None
    fpoc = None
    cpoc = []
    decisionMakers = []

    for key, value in lContactTypes.items():
        if "PPOC1" in value[0] and ppoc1 is None:
            name = " ".join(key)
            ppoc1 = f"Who is our primary point of contact? {name}\n"
        if "PPOC2" in value[0] and ppoc2 is None:
            name = " ".join(key)
            ppoc2 = f"If that person isn’t available, who should we consider our secondary point of contact? {name}\n"
        if "PPOC3" in value[0] and ppoc3 is None:
            name = " ".join(key)
            ppoc3 = f"If that person isn’t available, who should we consider our third point of contact? {name}\n"
        if "EPOC1" in value[0] and epoc1 is None:
            name = " ".join(key)
            epoc1 = f"If there is an issue after-hours, who should we contact? {name}\n"
        if "EPOC2" in value[0] and epoc2 is None:
            name = " ".join(key)
            epoc2 = f"If that person isn’t available, who should we consider our secondary after-hours point of contact? {name}\n"
        if "EPOC3" in value[0] and epoc3 is None:
            name = " ".join(key)
            epoc3 = f"If that person isn’t available, who should we consider our third after-hours point of contact?  {name}\n"
        if "FPOC" in value[0] and fpoc is None:
            name = " ".join(key)
            fpoc = f"Who should we consider to be our Accounts Payable point of contact? {name}\n"
        if "CPOC" in value[0]:
            cpoc.append(" ".join(key))
            cpocMsg = f"Who should we consider to be the senior leadership or management team? {', '.join(cpoc)}\n"
        if "Decision Maker" in value[0]:
            decisionMakers.append(" ".join(key))
            decisionMakersMsg = f"Who should we consider to be the decision makers in the business when it comes to IT? {', '.join(decisionMakers)}"

    message = ppoc1 + ppoc2 + ppoc3 + epoc1 + epoc2 + epoc3 + fpoc + cpocMsg + decisionMakersMsg
    print(message)

def main():
    lContactData = getDataInput()
    lContactTypes = contactTypeList(lContactData) 
    pocTypes(lContactTypes)
    lRemoteAuth = remoteAuthList(lContactData)
    remoteAuth(lRemoteAuth)
    lOnsiteAuth = onsiteAuthList(lContactData)
    onsiteAuth(lOnsiteAuth)
    lEmergencyAuth = emergencyAuthList(lContactData)
    emergencyAuth(lEmergencyAuth)
    lNonIncludedAuth = nonIncludedAuthList(lContactData)
    nonIncludedAuth(lNonIncludedAuth)
    lSecurityAuth = securityAuthList(lContactData)
    securityAuth(lSecurityAuth)
    lSecureUsers = secureUsersList(lContactData)
    secureUsers(lSecureUsers)
    lSpendingLimit = spendingLimitList(lContactData)
    spendingLimit(lSpendingLimit)

main()