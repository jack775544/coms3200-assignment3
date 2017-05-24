Write-Host -ForegroundColor Yellow "HTTP File. Will Succeed"
Write-Host "python .\webget.py http://www.rfc-base.org/txt/rfc-768.txt"
& python .\webget.py http://www.rfc-base.org/txt/rfc-768.txt
Write-Host ""

Write-Host -ForegroundColor Yellow "FTP File. Will Succeed"
Write-Host "python .\webget.py ftp://ftp.uq.edu.au/welcome.msg"
& python .\webget.py ftp://ftp.uq.edu.au/welcome.msg
Write-Host ""

Write-Host -ForegroundColor Yellow "FTP File. Will succeed"
Write-Host "python .\webget.py ftp://ftp.marine.csiro.au/pub/spencer_gulf/met/README"
& python .\webget.py ftp://ftp.marine.csiro.au/pub/spencer_gulf/met/README
Write-Host ""

Write-Host -ForegroundColor Yellow "FTP File. File not found"
Write-Host "python .\webget.py ftp://ftp.uq.edu.au/welcome.txt"
& python .\webget.py ftp://ftp.uq.edu.au/welcome.txt
Write-Host ""

Write-Host -ForegroundColor Yellow "FTP File. Wrong folder"
Write-Host "python .\webget.py ftp://ftp.uq.edu.au/toplevel/welcome.msg"
& python .\webget.py ftp://ftp.uq.edu.au/toplevel/welcome.msg
Write-Host ""

Write-Host -ForegroundColor Yellow "FTP File. Incorrect Hostname"
Write-Host "python .\webget.py ftp://ftp.itee.uq.edu.au/welcome.msg"
& python .\webget.py ftp://ftp.itee.uq.edu.au/welcome.msg
Write-Host ""

Write-Host -ForegroundColor Yellow "Unimplemented Protocol"
Write-Host "python .\webget.py ftps://ftp.uq.edu.au/welcome.msg"
& python .\webget.py ftps://ftp.uq.edu.au/welcome.msg