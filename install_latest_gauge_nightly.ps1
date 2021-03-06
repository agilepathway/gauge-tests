$gauge_latest_nightly_version=Invoke-WebRequest -Uri https://bintray.com/gauge/Gauge/Nightly/_latestVersion -MaximumRedirection 0 -ErrorAction Ignore -UseBasicParsing | %{$_.Headers.Location} | Split-Path -Leaf

if ([Environment]::Is64BitOperatingSystem) {
    $bit="x86_64"
}
else {
    $bit="x86"
}

$gauge_file_name="gauge-$($gauge_latest_nightly_version)-windows.$($bit).zip"

Invoke-WebRequest -Uri "https://bintray.com/gauge/Gauge/download_file?file_path=windows%2F$gauge_file_name" -OutFile $gauge_file_name

Write-Host "Unziping zip to $($env:GAUGE_PREFIX)"

Expand-Archive $gauge_file_name -DestinationPath $env:GAUGE_PREFIX

Write-Host "Done."