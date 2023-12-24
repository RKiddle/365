<#
There's two pieces of data that are required to assign an admin role to a user:

The object ID of the user.
The object ID of the role.
Once you know this information, you can then use the Add-AzureADDirectoryRoleMember cmdlet to assign a user to an admin role.
#>

Add-AzureADDirectoryRoleMember -ObjectID <ObjectID of the role> -RefObjectId <ObjectID of the user>

Get-AzureADUser -ObjectID "PattF@contoso.com"

Add-AzureADDirectoryRoleMember -ObjectID
