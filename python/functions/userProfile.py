def buildProfile(first, last, **usrInfo):
    """build a dictionary containing everything we know about a user"""
    profile = {}
    profile['firstName'] = first
    profile['lastName'] = last
    for key, value in usrInfo.items():
        profile[key] = value
    return profile


userProfile = buildProfile(
    'albert', 'einstein', location='princeton', field='physics')
print(userProfile)
