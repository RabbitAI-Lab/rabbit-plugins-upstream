#!/usr/bin/env node
"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
const fs = __importStar(require("fs"));
const path = __importStar(require("path"));
const dispatcher_1 = require("./dispatcher");
async function readStdin() {
    const chunks = [];
    for await (const chunk of process.stdin)
        chunks.push(Buffer.from(chunk));
    return Buffer.concat(chunks).toString("utf-8");
}
function attachLocalFile(request) {
    const params = { ...(request.params || {}) };
    const filePath = typeof params.filePath === "string"
        ? params.filePath
        : (typeof params.file === "string" ? params.file : null);
    if (!filePath)
        return { ...request, params };
    const absolutePath = path.resolve(filePath);
    const stat = fs.statSync(absolutePath);
    if (!stat.isFile())
        throw new Error("filePath 必须指向普通文件");
    params.file = {
        name: path.basename(absolutePath),
        size: stat.size,
        data: fs.createReadStream(absolutePath),
    };
    delete params.filePath;
    return { ...request, params };
}
async function main() {
    try {
        const input = (await readStdin()).trim();
        if (!input)
            throw new Error("请通过标准输入提供 JSON 请求");
        const request = attachLocalFile(JSON.parse(input));
        const result = await (0, dispatcher_1.invoke)(request);
        process.stdout.write(`${JSON.stringify(result)}\n`);
        if (result.code !== 200)
            process.exitCode = 1;
    }
    catch (error) {
        process.stdout.write(`${JSON.stringify({ code: -200, message: error?.message || "请求解析失败" })}\n`);
        process.exitCode = 1;
    }
}
void main();
//# sourceMappingURL=cli.js.map