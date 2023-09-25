function getIP {
    (get-netipaddress).ipv4address | Select-String "192*"
}

$IP = getIP

Write-Host("This machine's IP is $IP")
Write-Host("This machine's IP is {0}" -f $IP)

$User = $env:Username
$ver = $HOST.Version
$UserHost = $env:COMPUTERNAME
$DATE = Get-Date

$BODY = "This machine's IP is $IP. User is $User. Hostname is $UserHost. PowerShell $ver. Today's Date is $DATE."

Write-Host($BODY)

Send-MailMessage -To "dejarnke@mail.uc.edu" -From "ktbtut@gqmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)