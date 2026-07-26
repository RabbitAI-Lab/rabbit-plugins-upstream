// 同步结果统计：控制台输出 + GitHub Actions step summary。
import fs from "node:fs";

export class SyncStats {
  constructor(source) {
    this.source = source;
    this.added = 0;
    this.updated = 0;
    this.unchanged = 0;
    this.removed = 0;
    this.failed = 0;
    this.errors = [];
  }
  record(result) {
    if (result === "added") this.added++;
    else if (result === "updated") this.updated++;
    else this.unchanged++;
  }
  fail(id, err) {
    this.failed++;
    this.errors.push(`${id}: ${String(err.message || err).slice(0, 200)}`);
  }
  report() {
    const line =
      `[${this.source}] added=${this.added} updated=${this.updated} ` +
      `unchanged=${this.unchanged} removed=${this.removed} failed=${this.failed}`;
    console.log(line);
    if (this.errors.length) {
      console.warn(`[${this.source}] 失败明细（前 20 条）:`);
      for (const e of this.errors.slice(0, 20)) console.warn(`  - ${e}`);
    }
    if (process.env.GITHUB_STEP_SUMMARY) {
      const md =
        `### ${this.source}\n\n` +
        `- 新增: ${this.added} / 更新: ${this.updated} / 未变: ${this.unchanged} / 删除: ${this.removed} / 失败: ${this.failed}\n` +
        (this.errors.length
          ? `\n失败（前 20 条）:\n` + this.errors.slice(0, 20).map((e) => `- \`${e}\``).join("\n") + "\n"
          : "");
      fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, md);
    }
  }
}
