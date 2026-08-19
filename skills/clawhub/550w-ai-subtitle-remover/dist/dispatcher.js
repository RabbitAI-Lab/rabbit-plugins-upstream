"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.invoke = invoke;
const types_1 = require("./types");
const credential_manager_1 = require("./credential-manager");
const api_client_1 = require("./api-client");
const upload_video_1 = require("./actions/upload-video");
const submit_task_1 = require("./actions/submit-task");
const task_detail_1 = require("./actions/task-detail");
const task_list_1 = require("./actions/task-list");
const query_credits_1 = require("./actions/query-credits");
const workflow_engine_1 = require("./workflow-engine");
const remove_video_watermark_1 = require("./actions/remove-video-watermark");
const remove_image_watermark_1 = require("./actions/remove-image-watermark");
const image_watermark_task_detail_1 = require("./actions/image-watermark-task-detail");
const validator_1 = require("./validator");
const error_handler_1 = require("./error-handler");
async function invoke(request) {
    const credentialManager = new credential_manager_1.CredentialManager();
    if (request.action === "configureCredentials") {
        const params = request.params || {};
        const validationError = (0, validator_1.validateCredential)(params.userNo, params.apiKey);
        if (validationError)
            return validationError;
        try {
            const candidate = { userNo: params.userNo.trim(), apiKey: params.apiKey.trim() };
            const verification = await new api_client_1.ApiClient(candidate).post("/open/queryCredits", {}, types_1.TIMEOUT_CONFIG.query);
            if (verification.code !== types_1.ErrorCode.SUCCESS)
                return (0, error_handler_1.mapApiError)(verification);
            credentialManager.set(candidate);
            return { code: types_1.ErrorCode.SUCCESS, message: "凭证验证并配置成功", userNo: verification.userNo };
        }
        catch {
            return { code: types_1.ErrorCode.SERVER_ERROR, message: "凭证保存失败，请检查 Skill 目录写入权限" };
        }
    }
    if (!credentialManager.isConfigured()) {
        return credentialManager.getGuideMessage();
    }
    const validActions = ["uploadVideo", "submitTask", "taskDetail", "taskList", "queryCredits", "removeVideoWatermark", "removeImageWatermark", "imageWatermarkTaskDetail", "workflow"];
    if (!validActions.includes(request.action)) {
        return { code: types_1.ErrorCode.INVALID_PARAMS, message: `不支持的 action: ${request.action}` };
    }
    const credential = credentialManager.get();
    const client = new api_client_1.ApiClient(credential);
    switch (request.action) {
        case "uploadVideo": return (0, upload_video_1.uploadVideo)(request.params, client);
        case "submitTask": return (0, submit_task_1.submitTask)(request.params, client);
        case "taskDetail": return (0, task_detail_1.taskDetail)(request.params, client);
        case "taskList": return (0, task_list_1.taskList)(request.params, client);
        case "queryCredits": return (0, query_credits_1.queryCredits)(request.params, client);
        case "removeVideoWatermark": return (0, remove_video_watermark_1.removeVideoWatermark)(request.params, client);
        case "removeImageWatermark": return (0, remove_image_watermark_1.removeImageWatermark)(request.params, client);
        case "imageWatermarkTaskDetail": return (0, image_watermark_task_detail_1.imageWatermarkTaskDetail)(request.params, client);
        case "workflow": return (0, workflow_engine_1.executeWorkflow)(request.params, client);
        default: return { code: types_1.ErrorCode.INVALID_PARAMS, message: `不支持的 action: ${request.action}` };
    }
}
//# sourceMappingURL=dispatcher.js.map