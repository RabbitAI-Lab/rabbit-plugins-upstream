# Blender MCP v2.5.1 Publish Script
$ErrorActionPreference = "Stop"

$skillDir = "H:\OpenClaw\.openclaw\agents\bge\workspace\skills\blender-mcp"
Set-Location $skillDir

Write-Host "=== Publishing blender-mcp v2.5.1 to GitHub ===" -ForegroundColor Cyan

# Step 1: Publish SKILL.md
Write-Host "`n[1/4] Publishing SKILL.md..." -ForegroundColor Yellow
$skillBytes = [System.IO.File]::ReadAllBytes("$skillDir\SKILL.md")
$skillBase64 = [Convert]::ToBase64String($skillBytes)
$skillRemoteSha = gh api repos/taosiuman/blender-skill/contents/SKILL.md --jq '.sha'
$skillPayload = @{
    message = "v2.5.1: 5.3 Alpha API 增量更新 (18 项新增)"
    content = $skillBase64
    sha = $skillRemoteSha
} | ConvertTo-Json
[System.IO.File]::WriteAllText("$skillDir\_payload_skill.json", $skillPayload)
$skillResultSha = gh api repos/taosiuman/blender-skill/contents/SKILL.md -X PUT --input "$skillDir\_payload_skill.json" --jq '.content.sha'
Write-Host "✓ SKILL.md published: $skillResultSha" -ForegroundColor Green

# Step 2: Publish README.md
Write-Host "`n[2/4] Publishing README.md..." -ForegroundColor Yellow
$readmeBytes = [System.IO.File]::ReadAllBytes("$skillDir\README.md")
$readmeBase64 = [Convert]::ToBase64String($readmeBytes)
$readmeRemoteSha = gh api repos/taosiuman/blender-skill/contents/README.md --jq '.sha'
$readmePayload = @{
    message = "docs: update README for v2.5.1"
    content = $readmeBase64
    sha = $readmeRemoteSha
} | ConvertTo-Json
[System.IO.File]::WriteAllText("$skillDir\_payload_readme.json", $readmePayload)
$readmeResultSha = gh api repos/taosiuman/blender-skill/contents/README.md -X PUT --input "$skillDir\_payload_readme.json" --jq '.content.sha'
Write-Host "✓ README.md published: $readmeResultSha" -ForegroundColor Green

# Step 3: Update Git Tag
Write-Host "`n[3/4] Updating Git tag v2.5.1..." -ForegroundColor Yellow
$latestSha = gh api repos/taosiuman/blender-skill/commits/main --jq '.sha'
gh api "repos/taosiuman/blender-skill/git/refs/tags/v2.5.1" -X PATCH -f sha="$latestSha" -F force=true
Write-Host "✓ Git tag v2.5.1 updated" -ForegroundColor Green

# Step 4: Create GitHub Release
Write-Host "`n[4/4] Creating GitHub Release v2.5.1..." -ForegroundColor Yellow
$releaseNotes = @"
## v2.5.1 - 5.3 Alpha API 增量更新

### 新增 API (18 项)

**Cycles 元数据属性:**
- BatchRenameAction.name
- CyclesCurveRenderSettings.name, CyclesCustomCameraSettings.name
- CyclesLightSettings.name, CyclesMaterialSettings.name, CyclesMeshSettings.name
- CyclesObjectSettings.name, CyclesRenderLayerSettings.name, CyclesRenderSettings.name
- CyclesView3DShadingSettings.name, CyclesVisibilitySettings.name, CyclesWorldSettings.name

**其他新增:**
- GLTF2_filter_action.name
- NodeSetting.name
- Paint.show_auto_smooth_curve, Paint.show_hardness_curve, Paint.show_spacing_curve
- CompositorStrip.properties
- SequencerTimelineOverlay.show_thumbnails

### 变更类型
✅ 均为小功能增强，无破坏性变更
✅ 与 v2.5.0 完全向后兼容

---

**研究日期**: 2026-09-09 13:09
**数据来源**: Blender 官方 API change_log (5.2 to 5.3)
"@

[System.IO.File]::WriteAllText("$skillDir\release_notes.md", $releaseNotes)
gh release create v2.5.1 --repo taosiuman/blender-skill --title "v2.5.1 - 5.3 Alpha API 增量更新" --notes-file "$skillDir\release_notes.md" --latest
Write-Host "✓ GitHub Release v2.5.1 created" -ForegroundColor Green

# Cleanup
Write-Host "`n[Cleanup] Removing temporary files..." -ForegroundColor Yellow
Remove-Item "$skillDir\_payload_skill.json", "$skillDir\_payload_readme.json", "$skillDir\release_notes.md" -ErrorAction SilentlyContinue
Write-Host "✓ Cleanup complete" -ForegroundColor Green

Write-Host "`n=== Publish Summary ===" -ForegroundColor Cyan
Write-Host "GitHub SKILL.md SHA: $skillResultSha"
Write-Host "GitHub README SHA: $readmeResultSha"
Write-Host "GitHub Release: https://github.com/taosiuman/blender-skill/releases/tag/v2.5.1"
Write-Host "Git Tag: v2.5.1"
Write-Host "`n✓ All GitHub operations completed successfully!" -ForegroundColor Green
