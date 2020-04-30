Import-Csv -Path ./csvs/SIT110.csv | foreach {Add-TeamUser -GroupId e9456f3d-0a85-4adf-85c5-8cf0a978e781 -user $_.email}
