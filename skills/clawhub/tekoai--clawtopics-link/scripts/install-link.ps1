[CmdletBinding()]
param(
    [switch]$VerifyOnly
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"
$Version = "0.1.0"
$BaseUrl = "https://openclaw.tekoai.com/clawtopics-link/releases/v$Version"

$DetectedArchitecture = $env:PROCESSOR_ARCHITEW6432
if ([string]::IsNullOrWhiteSpace($DetectedArchitecture)) {
    $DetectedArchitecture = $env:PROCESSOR_ARCHITECTURE
}
$Architecture = switch ($DetectedArchitecture.ToUpperInvariant()) {
    "AMD64" { "amd64" }
    "ARM64" { "arm64" }
    default { throw "Unsupported Windows CPU architecture." }
}

$Metadata = @{
    "amd64" = @{
        Sha256 = "c53980a7a709504b58d4bac5fd6cb822b7bb93a852f2703c86414cf837a98eee"
        Size = 3057669
    }
    "arm64" = @{
        Sha256 = "4ac739b9c04a3df0dcad638b55bafffd7bbc23bcfd8dadca36e010d2c871eb2f"
        Size = 2738856
    }
}

$Artifact = "clawtopics-link_${Version}_windows_${Architecture}.zip"
$Url = "$BaseUrl/$Artifact"
$ParsedUrl = [System.Uri]$Url
if ($ParsedUrl.Scheme -ne "https" -or $ParsedUrl.Host -ne "openclaw.tekoai.com") {
    throw "Refusing a non-official Link URL."
}

$TemporaryDirectory = Join-Path ([System.IO.Path]::GetTempPath()) (
    "clawtopics-link-" + [System.Guid]::NewGuid().ToString("N")
)
[System.IO.Directory]::CreateDirectory($TemporaryDirectory) | Out-Null

try {
    $ArchivePath = Join-Path $TemporaryDirectory $Artifact
    Invoke-WebRequest `
        -Uri $Url `
        -OutFile $ArchivePath `
        -MaximumRedirection 0 `
        -UseBasicParsing

    $Archive = Get-Item -LiteralPath $ArchivePath
    if ($Archive.Length -ne $Metadata[$Architecture].Size) {
        throw "Artifact size verification failed."
    }
    $ActualHash = (Get-FileHash -LiteralPath $ArchivePath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($ActualHash -ne $Metadata[$Architecture].Sha256) {
        throw "Artifact SHA-256 verification failed."
    }

    $ExtractedDirectory = Join-Path $TemporaryDirectory "extracted"
    Expand-Archive -LiteralPath $ArchivePath -DestinationPath $ExtractedDirectory
    $Files = @(Get-ChildItem -LiteralPath $ExtractedDirectory -File -Recurse)
    $ExpectedBinary = Join-Path $ExtractedDirectory "clawtopics-link.exe"
    if ($Files.Count -ne 1 -or $Files[0].FullName -ne $ExpectedBinary) {
        throw "Artifact contains an unexpected path."
    }

    $ActualVersion = (& $ExpectedBinary version | Out-String).Trim()
    if ($LASTEXITCODE -ne 0 -or $ActualVersion -ne $Version) {
        throw "Link version verification failed."
    }

    if ($VerifyOnly) {
        Write-Output "Verified ClawTopics Link $Version for windows/$Architecture."
        return
    }

    $LocalAppData = [Environment]::GetFolderPath("LocalApplicationData")
    if ([string]::IsNullOrWhiteSpace($LocalAppData)) {
        throw "A valid LocalAppData directory is required."
    }
    $DestinationDirectory = Join-Path $LocalAppData "TekoAI\ClawTopics Link\bootstrap"
    [System.IO.Directory]::CreateDirectory($DestinationDirectory) | Out-Null
    $Destination = Join-Path $DestinationDirectory "clawtopics-link.exe"
    $StagedDestination = "$Destination.new"
    Copy-Item -LiteralPath $ExpectedBinary -Destination $StagedDestination -Force
    Move-Item -LiteralPath $StagedDestination -Destination $Destination -Force
    Write-Output "Installed verified ClawTopics Link $Version`: $Destination"
}
finally {
    if (Test-Path -LiteralPath $TemporaryDirectory) {
        Remove-Item -LiteralPath $TemporaryDirectory -Recurse -Force
    }
}
