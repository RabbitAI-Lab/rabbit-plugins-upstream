import { type PluginConfig } from "./api.js";
export declare const UPLOAD_TOOL = "adaptlypost_upload_media";
export declare const CREATE_POST_TOOL = "adaptlypost_create_post";
export declare const RETRY_TOOL = "adaptlypost_retry_failed";
export declare const GATED_TOOLS: readonly ["adaptlypost_upload_media", "adaptlypost_create_post", "adaptlypost_retry_failed"];
export declare const APPROVAL_TIMEOUT_MS = 300000;
export type PostMode = "DRAFT" | "SCHEDULE" | "PUBLISH_NOW";
export type ApprovalRequest = {
    title: string;
    description: string;
    severity: "info" | "warning" | "critical";
    scope: {
        kind: "external-post";
        target: string;
        visibility: "public" | "restricted";
    };
};
export declare class ApprovalLedger {
    private readonly grants;
    grant(toolCallId: string, params: unknown): void;
    consume(toolCallId: string, toolName: string, params: unknown): void;
}
export declare function buildPostBody(params: Record<string, unknown>): Record<string, unknown>;
export declare function describeApproval(cfg: PluginConfig, toolName: string, params: Record<string, unknown>): Promise<ApprovalRequest | undefined>;
