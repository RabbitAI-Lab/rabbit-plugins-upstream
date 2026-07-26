/**
 * qrcode.js — QR Code Generator for Travel Planner
 *
 * 生成支付二维码，用于行程网页中的扫码支付功能
 *
 * 用法：
 *   node scripts/qrcode.js <url> [outputPath]
 *
 * 示例：
 *   node scripts/qrcode.js "https://example.com/payment" ./output/qr.png
 */

const QRCode = require('qrcode');
const path = require('path');
const fs = require('fs');

async function generateQR(text, outputPath) {
  try {
    // 确保输出目录存在
    const dir = path.dirname(outputPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    await QRCode.toFile(outputPath, text, {
      color: {
        dark: '#000000',
        light: '#ffffff'
      },
      width: 400,
      margin: 2,
      errorCorrectionLevel: 'M'
    });

    console.log(`✅ 二维码已生成：${outputPath}`);
    return outputPath;
  } catch (err) {
    console.error('❌ 二维码生成失败：', err.message);
    return null;
  }
}

async function generateQRBase64(text) {
  try {
    const dataUrl = await QRCode.toDataURL(text, {
      color: { dark: '#000000', light: '#ffffff' },
      width: 300,
      margin: 2,
      errorCorrectionLevel: 'M'
    });
    return dataUrl;
  } catch (err) {
    console.error('❌ 二维码生成失败：', err.message);
    return null;
  }
}

// 命令行模式
if (require.main === module) {
  const args = process.argv.slice(2);
  const url = args[0];
  const outputPath = args[1] || path.join(process.cwd(), 'output', `qr-${Date.now()}.png`);

  if (!url) {
    console.error('用法：node scripts/qrcode.js <url> [outputPath]');
    console.error('示例：node scripts/qrcode.js "https://example.com" ./output/qr.png');
    process.exit(1);
  }

  generateQR(url, outputPath).then(result => {
    if (result) process.exit(0);
    else process.exit(1);
  });
}

module.exports = { generateQR, generateQRBase64 };