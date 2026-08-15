"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.probeVideoUrl = probeVideoUrl;
const child_process_1 = require("child_process");
/**
 * 使用本机 ffprobe 获取远程视频的真实元信息。不得伪造默认宽高和时长：这些字段既参与
 * 服务端快速拒绝，也可能在远程媒体暂时无法探测时成为兜底依据。
 */
async function probeVideoUrl(videoUrl) {
    const ffprobe = process.env.FFPROBE_PATH?.trim() || "ffprobe";
    const args = [
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height:format=duration",
        "-of", "json",
        videoUrl,
    ];
    return new Promise((resolve, reject) => {
        (0, child_process_1.execFile)(ffprobe, args, { timeout: 20000, maxBuffer: 1024 * 1024 }, (error, stdout) => {
            if (error) {
                reject(new Error(`无法预检远程视频，请确认链接可访问且已安装 ffprobe：${error.message}`));
                return;
            }
            try {
                const payload = JSON.parse(stdout);
                const stream = payload?.streams?.[0];
                const width = Number(stream?.width);
                const height = Number(stream?.height);
                const duration = Math.ceil(Number(payload?.format?.duration));
                if (!Number.isFinite(width) || !Number.isFinite(height) || !Number.isFinite(duration)
                    || width <= 0 || height <= 0 || duration <= 0) {
                    throw new Error("未读取到有效的视频宽高或时长");
                }
                resolve({ width, height, duration });
            }
            catch (parseError) {
                reject(new Error(`远程视频预检结果无效：${parseError?.message || "未知错误"}`));
            }
        });
    });
}
//# sourceMappingURL=video-probe.js.map