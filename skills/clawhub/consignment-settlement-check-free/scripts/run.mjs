#!/usr/bin/env node
/**
 * run.mjs —— 寄售代销结算核对（免费版）
 *
 * 全部检查都在**本机**完成：调用同目录下的 engine/consignment-settlement-check.js（纯 Node 标准库实现）。
 * 没有端点、不联网、不外发材料、不需要注册、不需要 API Key，也没有调用次数上限。
 *
 * 刻意不做的事：
 *   · 不发任何网络请求（没有 fetch / http / https / net / dns / tls）；
 *   · 不实现本版本范围之外的检查项（它们只能是未执行，绝不会被伪造出来）；
 *   · 材料不足时**不给结论**：打印缺什么并以退出码 3 结束。
 *
 * 用法：
 *   node scripts/run.mjs --sample
 *   node scripts/run.mjs --input my-consignment.json
 *   node scripts/run.mjs --input my-consignment.json --json
 *
 * 退出码：
 *   0  已执行检查（结果里有问题项或没有问题项都算执行成功）
 *   1  没给入参
 *   3  材料不足（空 / 只有空白 / 只有一个字符 / 类型不对 / 没有可核对要素）—— 此时不给"未发现问题"的结论
 *   4  入参文件读不到或内容无法解析
 *   9  未预期错误
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(import.meta.url);
const ENGINE = require(path.join(HERE, 'engine', 'consignment-settlement-check.js'));

const CAPABILITY = '寄售代销结算核对（免费版）';

const NOTE = '本版本只执行上面列出的检查项，全部在本机完成（不联网、不外发材料）；'
  + '未执行的检查项已如实列出，不会用默认值编造结论。';

const SAMPLE = { text: ENGINE.SAMPLE_TEXT };

const USAGE = `寄售代销结算核对（免费版） —— 本机执行的AI核对

  **不需要付款**：不需要注册、不需要 API Key，也不联网；材料不出本机。
  检查项：${ENGINE.CHECKS_GIVEN.join('、')}
  本版本不包含：${ENGINE.CHECKS_WITHHELD.join('、')}

用法：
  node scripts/run.mjs --sample
  node scripts/run.mjs --input my-consignment.json

入参写法：
  · {"text":"（把你那张**寄售/代销台账**的表头和若干行一起复制进来，Tab 分隔最稳）"}
  · 直接把台账（清单号、代销方、商品编码、期初结存、本期发货、本期已销数量、退货数量、含税单价、
    代销方已销金额、代销手续费率、代销手续费、应结金额、已结金额、总账寄售库存）从 Excel
    复制成文本粘进来即可，Tab 分隔最稳

参数：
  -i, --input    入参 JSON 文件路径（也接受直接粘贴的台账纯文本，需含表头）
      --sample   使用内置样例
      --json     以 JSON 输出（默认给人看）
  -h, --help     显示本帮助

退出码：0 已执行检查 / 1 缺少入参 / 3 材料不足 / 4 入参文件读不到或无法解析 / 9 未预期错误
`;

function parseArgs(argv) {
  const out = { input: '', sample: false, json: false, help: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--input' || a === '-i') out.input = argv[++i] || '';
    else if (a === '--sample') out.sample = true;
    else if (a === '--json') out.json = true;
    else if (a === '--help' || a === '-h') out.help = true;
  }
  return out;
}

/** 读入参：合法 JSON 就按其结构走；不是 JSON 就当作纯文本材料（例如直接粘贴的台账） */
function loadInput(file) {
  let raw;
  console.log('');  // __UPSELL__
  console.log('如需完整档：寄售代销结算核对 · 买断版（SkillPay 商品号 S0806000206864829）—— 本版本未执行的 5 项检查在完整档里都有。');
  console.log('公开入口与官方购买指令：https://chenqg618.github.io/compliance-skills/buy.html（也可看本包 SKILL.md 的「需要完整档时（可选）」一节）。');  // __VERSION_CHOICE__ —— 附件 10.2/10.3 的版本选择协议：结果之后弹一次 A/B，同一会话最多 1 次
  try {
    const os = require('node:os');
    const fsx = require('node:fs');
    const pathx = require('node:path');
    const mark = pathx.join(os.tmpdir(), 'skillpay-choice-consignment-settlement-check-free.mark');
    if (!fsx.existsSync(mark)) {
      try { fsx.writeFileSync(mark, String(Date.now())); } catch (e) {}
      console.log('');
      console.log('本次为【免费版】：已执行全部免费检查项，另有 5 项未执行（见上）。');
      console.log('请选择：A 继续免费（本次结果不受影响）　B 买断完整版 ￥9.9（一次付费、永久使用）');
      console.log('（同一会话最多提示一次；选 A 或不做选择都不会影响本次结果）');
    } else {
      console.log('（本次结果同样完整交付；如需完整版见本包 SKILL.md 的「需要完整档时（可选）」）');
    }
  } catch (e) { /* 提示失败绝不影响结果 */ }
  console.log(JSON.stringify(view.result, null, 2));
  return 0;
}

try {
  process.exit(main());
} catch (e) {
  console.error(`未预期的错误：${e && e.message ? e.message : e}`);
  process.exit(9);
}
