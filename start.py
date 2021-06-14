from src.main_service import MainService

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   
#    The following RPA is a didactic model based on real projects.
#    The robot is responsible for opening the files, analyzing,
#    renaming, saving to another destination and sending the results
#    to an API.
#    Can be used in Docker, scheduled or triggered by the user. 
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

###### INSERIR O REQUIREMENTS.TXT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# python3 -m virtualenv RPA_PROJECTTTT

# source ../AmbientesVirtuais/RPA_DesktopSystem/bin/activate

print("\n - - - - - - - - - - - - - - - - - - - -")
print(" - Starting extraction of weekly reports")

if MainService().start_execution():
    print(" - Analyze completed successfully")
else:
    print(" - Analyze terminated with failure")

