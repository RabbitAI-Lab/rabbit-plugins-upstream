export declare const API_BASE_URL = "https://post.adaptlypost.com/post/api/v1";
export type PluginConfig = {
    apiToken?: string;
    mediaDirs?: string[];
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
export type LocalMediaFile = {
    path: string;
    size: number;
};
export declare function resolveLocalMedia(cfg: PluginConfig, filePath: string): Promise<LocalMediaFile>;
export declare function describeLocalMedia(file: LocalMediaFile): string;
export declare function uploadLocalFile(cfg: PluginConfig, filePath: string, signal?: AbortSignal): Promise<UploadedMedia>;
export declare function parseRemoteUrl(raw: string): URL;
export declare function describeRemoteUrl(url: URL): string;
export declare function uploadRemoteUrl(cfg: PluginConfig, sourceUrl: string, signal?: AbortSignal): Promise<UploadedMedia>;
export {};
