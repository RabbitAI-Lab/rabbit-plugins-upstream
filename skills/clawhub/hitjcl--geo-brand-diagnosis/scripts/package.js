const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const skillDir = 'C:\\Users\\hitjc\\qclaw\\workspace\\geo-brand-diagnosis-skill';
const outputPath = 'C:\\Users\\hitjc\\qclaw\\workspace\\geo-brand-diagnosis-v1.0.skill';

// Remove old output
if (fs.existsSync(outputPath)) fs.unlinkSync(outputPath);

// Create zip (tar in practice uses node's built-in)
// We'll use powershell Compress-Archive
const tmpZip = 'C:\\Users\\hitjc\\qclaw\\workspace\\geo-brand-diagnosis-skill.zip';
if (fs.existsSync(tmpZip)) fs.unlinkSync(tmpZip);

try {
  execSync(`powershell -NoProfile -Command "Compress-Archive -Path '${skillDir}\\*' -DestinationPath '${tmpZip}' -Force"`, { stdio: 'inherit' });
  fs.renameSync(tmpZip, outputPath);
  console.log(`✅ Skill 打包成功: ${outputPath}`);
  console.log(`📦 大小: ${(fs.statSync(outputPath).size / 1024).toFixed(1)} KB`);
} catch(e) {
  console.error('打包失败:', e.message);
}
