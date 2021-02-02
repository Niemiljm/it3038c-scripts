function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
    }
$IP = getIP
$Power = Get-Host | Select-Object Version
$Date = Get-Date -Format G
$EmailTo = "niemiljm@mail.uc.edu"
$EmailFrom = "joester4life97@gmail.com"
$Subject = "IT3038c Powershell Script"
$BODY = "This machine's IP is: $IP The User is an Administrator. The hostname is: $env:COMPUTERNAME. Powershell is running on version: $Power And today's date is: $Date "
$SMTPServer = "smtp.gmail.com"
$SMTPMessage = New-Object System.Net.Mail.MailMessage($EmailFrom,$EmailTo,$Subject,$Body)
$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587) 
$SMTPClient.EnableSsl = $true 
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential("joester4life97@gmail.com", "lhwjluijovurygyp");
$SMTPClient.Send($SMTPMessage)

