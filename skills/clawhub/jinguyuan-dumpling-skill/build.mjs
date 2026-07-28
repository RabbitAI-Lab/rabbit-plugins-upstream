#!/usr/bin/env node
/**
 * 紧凑发布构建（docs/COMPACT-RELEASE-PLAN.md）
 *
 * 开发松散、发布融合：把 scripts/cli.js（统一入口）连同金谷园自有模块与
 * qrcode 依赖树 bundle 成单文件 scripts/jgy.cjs；美团 pt-passport 是第三方
 * 预构建混淆件，仅通过 execFile 按文件路径调用，天然外置，不参与打包。
 *
 * 用法：
 *   node build.mjs            # 产出 build/compact/ 完整精简包
 *   node build.mjs --out DIR  # 指定输出目录
 *
 * 产物形态（安装态）：
 *   SKILL.md skill.json README.md LICENSE THIRD_PARTY_LICENSES.md
 *   references/*.md（命令路径已同步为 jgy.cjs）
 *   scripts/jgy.cjs + scripts/vendor/pt-passport/**
 *
 * 严禁手改产物 jgy.cjs：下次构建会覆盖。
 */
import { build } from 'esbuild';
import { cpSync, mkdirSync, rmSync, readFileSync, writeFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const argv = process.argv.slice(2);
const outIdx = argv.indexOf('--out');
const outDir = resolve(root, outIdx >= 0 ? argv[outIdx + 1] : 'build/compact');

rmSync(outDir, { recursive: true, force: true });
mkdirSync(join(outDir, 'scripts'), { recursive: true });

// 1) bundle 单文件 CLI
const result = await build({
  entryPoints: [join(root, 'scripts/cli.js')],
  outfile: join(outDir, 'scripts/jgy.cjs'),
  bundle: true,
  platform: 'node',
  target: 'node18',
  format: 'cjs',
  minify: false, // 明文可审计
  banner: { js: '/* 构建产物：由 build.mjs 从 scripts/ 松散模块融合生成，严禁手改。 */' },
  logLevel: 'silent',
  metafile: true,
  // vendored qrcode 内部的裸导入指向同层 bundled_modules（ClawHub 不允许 node_modules 目录名）
  alias: {
    dijkstrajs: join(root, 'scripts/vendor/bundled_modules/dijkstrajs'),
    pngjs: join(root, 'scripts/vendor/bundled_modules/pngjs'),
  },
});
const bundledInputs = Object.keys(result.metafile.inputs).length;

// 2) 外置件与静态文件
cpSync(join(root, 'scripts/vendor/pt-passport'), join(outDir, 'scripts/vendor/pt-passport'), { recursive: true });
cpSync(join(root, 'scripts/vendor/manifest.json'), join(outDir, 'scripts/vendor/manifest.json'));
// package.json 不随包：发布态无安装流程，engines 声明不生效；版本锚由 skill.json + SKILL.md 承担
for (const f of ['LICENSE', 'README.md', 'skill.json']) {
  cpSync(join(root, f), join(outDir, f));
}
mkdirSync(join(outDir, 'references'), { recursive: true });

// 3) 命令路径同步（有序规则）：
//    scripts/queue.js ... -> scripts/jgy.cjs queue ...；裸 queue.js -> jgy.cjs queue；jgy.js -> jgy.cjs
function transform(text) {
  return text
    .replaceAll('scripts/queue.js', 'scripts/jgy.cjs queue')
    .replaceAll('queue.js', 'jgy.cjs queue')
    .replaceAll('jgy.js', 'jgy.cjs');
}
writeFileSync(join(outDir, 'SKILL.md'), transform(readFileSync(join(root, 'SKILL.md'), 'utf8')));
for (const name of readdirSync(join(root, 'references'))) {
  if (!name.endsWith('.md')) continue;
  writeFileSync(join(outDir, 'references', name), transform(readFileSync(join(root, 'references', name), 'utf8')));
}

// 4) 第三方许可证清单
const manifest = JSON.parse(readFileSync(join(root, 'scripts/vendor/manifest.json'), 'utf8'));
writeFileSync(join(outDir, 'THIRD_PARTY_LICENSES.md'), `# 第三方组件清单

本 Skill 发布包中的 scripts/jgy.cjs 为构建产物（esbuild bundle，明文未混淆），融合了以下上游依赖：

| 组件 | 版本 | 许可证 | 说明 |
|---|---|---|---|
| qrcode | ${manifest.qrcode.version} | MIT | 二维码 PNG 生成（含依赖 pngjs/MIT、dijkstrajs/MIT），bundle 进 jgy.cjs |
| @mtuser/pt-passport | ${manifest.ptPassport.version} | 上游专有 | 美团 Passport 签名件，预构建混淆代码，原样外置于 scripts/vendor/pt-passport/，不参与 bundle；随包入口已移除后台守护/动态更新/http 全局拦截 |

金谷园自有代码以 MIT 许可发布（见 LICENSE）。上游完整性摘要见 scripts/vendor/manifest.json。
`);

console.log(JSON.stringify({ ok: true, outDir, bundledInputs, note: 'pt-passport 外置，references/SKILL.md 命令路径已同步' }));
