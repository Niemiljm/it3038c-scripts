
function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
    }

$IP = getIP
$NAME= Get-Content env:COMPUTERNAME
$Pow = Get-Host | Select-Object Version
$BODY= "This machine's IP is: $IP The User is an Administrator. The hostname is: ($env:COMPUTERNAME) "
Send-MailMessage -To "joester4life97@gmail.com" -From "niemiljm@mail.uc.edu" -Subject "IT3038C Windows SysInfo Test Information" -Body $BODY -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)