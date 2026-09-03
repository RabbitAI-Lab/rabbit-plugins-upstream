export type PluginConfig = {
    apiToken?: string;
    baseUrl?: string;
};
export declare function readConfig(api: {
    config?: unknown;
}): PluginConfig;
export declare function callApi(cfg: PluginConfig, method: "GET" | "POST" | "PATCH" | "DELETE", path: string, options?: {
    body?: unknown;
    query?: Record<string, unknown>;
    signal?: AbortSignal;
}): Promise<unknown>;
export declare const SUPPORTED_MIME_TYPES: string[];
type UploadedMedia = {
    publicUrl: string;
    key: string;
};
export declare function uploadLocalFile(cfg: PluginConfig, filePath: string, signal?: AbortSignal): Promise<UploadedMedia>;
export declare function uploadRemoteUrl(cfg: PluginConfig, sourceUrl: string, signal?: AbortSignal): Promise<UploadedMedia>;
export {};
