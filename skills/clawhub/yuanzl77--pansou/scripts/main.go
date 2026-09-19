// PanSou 网盘搜索 CLI —— Go 版（多站点并发、零依赖）。
//
// 环境变量:
//
//	PANSOU_URL    单个服务地址 (如 http://localhost:8888)，可选
//	PANSOU_URLS   多个服务地址，逗号分隔；设置后优先于 PANSOU_URL
//	PANSOU_USER   用户名 (认证启用时需要)
//	PANSOU_PWD    密码   (认证启用时需要)
//
// 搜索策略:
//
//	--strategy first  全部站点并发，谁先返回有效数据就先展示谁
//	--strategy merge  全部站点并发，等所有站点返回后按站点合并
//
// Token 存储在 ~/.config/pansou/token.json（单站点）或
// ~/.config/pansou/tokens/<host>.json（多站点）。
package main

import (
	"bytes"
	"encoding/json"
	"flag"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"sync"
	"time"
)

const (
	timeout             = 60 * time.Second
	probeTimeout        = 5 * time.Second
	healthWarnThreshold = 3
)

type serverConfig struct {
	urls     []string
	user     string
	password string
}

type searchOptions struct {
	channels   []string
	conc       int
	refresh    bool
	res        string
	src        string
	plugins    []string
	cloudTypes []string
	include    []string
	exclude    []string
	useGet     bool
}

type siteResult struct {
	url   string
	data  map[string]any
	error string
}

func loadConfig() serverConfig {
	urlsRaw := strings.TrimSpace(os.Getenv("PANSOU_URLS"))
	single := strings.TrimRight(os.Getenv("PANSOU_URL"), "/")

	var urls []string
	if urlsRaw != "" {
		for _, u := range strings.Split(urlsRaw, ",") {
			if u = strings.TrimSpace(u); u != "" {
				urls = append(urls, strings.TrimRight(u, "/"))
			}
		}
	}
	if single != "" {
		urls = append(urls, single)
	}

	seen := make(map[string]bool, len(urls))
	uniq := make([]string, 0, len(urls))
	for _, u := range urls {
		if !seen[u] {
			seen[u] = true
			uniq = append(uniq, u)
		}
	}
	return serverConfig{
		urls:     uniq,
		user:     os.Getenv("PANSOU_USER"),
		password: os.Getenv("PANSOU_PWD"),
	}
}

func tokenFileFor(cfg serverConfig, addr string) string {
	home, err := os.UserHomeDir()
	if err != nil {
		return ""
	}
	if len(cfg.urls) <= 1 {
		return filepath.Join(home, ".config", "pansou", "token.json")
	}
	host := addr
	if i := strings.Index(host, "//"); i >= 0 {
		host = host[i+2:]
	}
	var b strings.Builder
	for _, c := range host {
		switch {
		case c >= 'a' && c <= 'z', c >= 'A' && c <= 'Z', c >= '0' && c <= '9',
			c == '.', c == '_', c == '-':
			b.WriteRune(c)
		default:
			b.WriteRune('_')
		}
	}
	return filepath.Join(home, ".config", "pansou", "tokens", b.String()+".json")
}

func loadToken(cfg serverConfig, addr string) string {
	path := tokenFileFor(cfg, addr)
	if path == "" {
		return ""
	}
	data, err := os.ReadFile(path)
	if err != nil {
		return ""
	}
	var box struct {
		Token string `json:"token"`
	}
	if err := json.Unmarshal(data, &box); err != nil {
		return ""
	}
	return box.Token
}

func saveToken(cfg serverConfig, addr, token string) {
	path := tokenFileFor(cfg, addr)
	if path == "" {
		return
	}
	if err := os.MkdirAll(filepath.Dir(path), 0o700); err != nil {
		return
	}
	box := struct {
		Token string `json:"token"`
	}{Token: token}
	data, err := json.MarshalIndent(box, "", "  ")
	if err != nil {
		return
	}
	_ = os.WriteFile(path, data, 0o600)
}

func loginFor(cfg serverConfig, addr string) (string, error) {
	if cfg.user == "" || cfg.password == "" {
		return "", fmt.Errorf("%s 启用了认证，但未配置 PANSOU_USER / PANSOU_PWD", addr)
	}
	body, err := json.Marshal(map[string]string{"username": cfg.user, "password": cfg.password})
	if err != nil {
		return "", err
	}
	client := &http.Client{Timeout: timeout}
	resp, err := client.Post(addr+"/api/auth/login", "application/json", bytes.NewReader(body))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	var data map[string]any
	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		return "", fmt.Errorf("登录响应非 JSON")
	}
	if msg, ok := data["error"].(string); ok && msg != "" {
		return "", fmt.Errorf("登录失败: %s", msg)
	}
	token, _ := data["token"].(string)
	if token == "" {
		return "", fmt.Errorf("登录响应无 token")
	}
	saveToken(cfg, addr, token)
	return token, nil
}

func getToken(cfg serverConfig, addr string) (string, error) {
	if token := loadToken(cfg, addr); token != "" {
		return token, nil
	}
	return loginFor(cfg, addr)
}

func authHeader(token string) http.Header {
	h := http.Header{}
	h.Set("Content-Type", "application/json")
	h.Set("Accept", "application/json")
	h.Set("Authorization", "Bearer "+token)
	return h
}

func buildPayload(keyword string, o searchOptions) map[string]any {
	payload := map[string]any{"kw": keyword, "res": o.res, "src": o.src}
	if len(o.channels) > 0 {
		payload["channels"] = o.channels
	}
	if o.conc > 0 {
		payload["conc"] = o.conc
	}
	if o.refresh {
		payload["refresh"] = true
	}
	if len(o.plugins) > 0 {
		payload["plugins"] = o.plugins
	}
	if len(o.cloudTypes) > 0 {
		payload["cloud_types"] = o.cloudTypes
	}
	if len(o.include) > 0 || len(o.exclude) > 0 {
		f := map[string]any{}
		if len(o.include) > 0 {
			f["include"] = o.include
		}
		if len(o.exclude) > 0 {
			f["exclude"] = o.exclude
		}
		payload["filter"] = f
	}
	return payload
}

func buildQuery(keyword string, o searchOptions) string {
	params := url.Values{}
	params.Set("kw", keyword)
	params.Set("res", o.res)
	params.Set("src", o.src)
	if len(o.channels) > 0 {
		params.Set("channels", strings.Join(o.channels, ","))
	}
	if o.conc > 0 {
		params.Set("conc", strconv.Itoa(o.conc))
	}
	if o.refresh {
		params.Set("refresh", "true")
	}
	if len(o.plugins) > 0 {
		params.Set("plugins", strings.Join(o.plugins, ","))
	}
	if len(o.cloudTypes) > 0 {
		params.Set("cloud_types", strings.Join(o.cloudTypes, ","))
	}
	if len(o.include) > 0 || len(o.exclude) > 0 {
		f := map[string]any{}
		if len(o.include) > 0 {
			f["include"] = o.include
		}
		if len(o.exclude) > 0 {
			f["exclude"] = o.exclude
		}
		if data, err := json.Marshal(f); err == nil {
			params.Set("filter", string(data))
		}
	}
	return params.Encode()
}

// 部分部署把结果包在 {code, message, data} 信封里，这里拆掉外层。
func unwrapEnvelope(data map[string]any) (map[string]any, string) {
	inner, ok := data["data"].(map[string]any)
	if !ok {
		return data, ""
	}
	_, hasCode := data["code"]
	_, hasMsg := data["message"]
	if !hasCode && !hasMsg {
		return data, ""
	}
	if code, ok := data["code"].(float64); ok && code != 0 {
		msg, _ := data["message"].(string)
		if msg == "" {
			msg = fmt.Sprintf("code %v", code)
		}
		return nil, msg
	}
	return inner, ""
}

func searchURL(cfg serverConfig, addr, keyword string, o searchOptions) siteResult {
	client := &http.Client{Timeout: timeout}

	do := func(withAuth bool) (*http.Response, error) {
		if o.useGet {
			req, err := http.NewRequest("GET", addr+"/api/search?"+buildQuery(keyword, o), nil)
			if err != nil {
				return nil, err
			}
			if withAuth {
				token, err := getToken(cfg, addr)
				if err != nil {
					return nil, err
				}
				req.Header = authHeader(token)
			}
			return client.Do(req)
		}
		body, err := json.Marshal(buildPayload(keyword, o))
		if err != nil {
			return nil, err
		}
		req, err := http.NewRequest("POST", addr+"/api/search", bytes.NewReader(body))
		if err != nil {
			return nil, err
		}
		req.Header.Set("Content-Type", "application/json")
		req.Header.Set("Accept", "application/json")
		if withAuth {
			token, err := getToken(cfg, addr)
			if err != nil {
				return nil, err
			}
			req.Header.Set("Authorization", "Bearer "+token)
		}
		return client.Do(req)
	}

	resp, err := do(false)
	if err != nil {
		return siteResult{url: addr, error: err.Error()}
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusUnauthorized {
		resp.Body.Close()
		resp, err = do(true)
		if err != nil {
			return siteResult{url: addr, error: err.Error()}
		}
		defer resp.Body.Close()
	}

	var data map[string]any
	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		return siteResult{url: addr, error: fmt.Sprintf("HTTP %d 返回非 JSON", resp.StatusCode)}
	}

	data, envErr := unwrapEnvelope(data)
	if envErr != "" {
		return siteResult{url: addr, error: envErr}
	}
	if msg, ok := data["error"].(string); ok && msg != "" {
		return siteResult{url: addr, error: msg}
	}
	if resp.StatusCode >= 400 {
		return siteResult{url: addr, error: fmt.Sprintf("HTTP %d", resp.StatusCode)}
	}
	return siteResult{url: addr, data: data}
}

func resultCount(data map[string]any) int {
	if total, ok := data["total"].(float64); ok && total > 0 {
		return int(total)
	}
	if merged, ok := data["merged_by_type"].(map[string]any); ok {
		n := 0
		for _, v := range merged {
			if items, ok := v.([]any); ok {
				n += len(items)
			}
		}
		return n
	}
	if results, ok := data["results"].([]any); ok {
		return len(results)
	}
	return 0
}

func searchAll(cfg serverConfig, keyword string, o searchOptions, strategy string) map[string]any {
	if len(cfg.urls) == 1 {
		r := searchURL(cfg, cfg.urls[0], keyword, o)
		if r.data != nil {
			return r.data
		}
		return map[string]any{"url": r.url, "error": r.error}
	}

	ch := make(chan siteResult, len(cfg.urls))
	for _, u := range cfg.urls {
		go func(addr string) {
			ch <- searchURL(cfg, addr, keyword, o)
		}(u)
	}

	if strategy == "first" {
		var emptyFirst *siteResult
		got := 0
		for r := range ch {
			got++
			if r.data != nil && resultCount(r.data) > 0 {
				r.data["_site"] = r.url
				return r.data
			}
			if emptyFirst == nil {
				cp := r
				emptyFirst = &cp
			}
			if got == len(cfg.urls) {
				if emptyFirst != nil {
					return map[string]any{"url": emptyFirst.url, "error": emptyFirst.error}
				}
				return map[string]any{"error": "所有站点搜索均失败"}
			}
		}
	}

	sites := make(map[string]any, len(cfg.urls))
	for i := 0; i < len(cfg.urls); i++ {
		r := <-ch
		if r.data != nil {
			sites[r.url] = r.data
		} else {
			sites[r.url] = map[string]any{"error": r.error}
		}
	}
	return map[string]any{"strategy": "merge", "sites": sites}
}

func healthAll(cfg serverConfig) []map[string]any {
	client := &http.Client{Timeout: timeout}
	var mu sync.Mutex
	var wg sync.WaitGroup
	box := make(map[string]map[string]any, len(cfg.urls))

	for _, u := range cfg.urls {
		wg.Add(1)
		go func(addr string) {
			defer wg.Done()
			entry := map[string]any{"url": addr, "data": nil, "error": nil}
			resp, err := client.Get(addr + "/api/health")
			if err != nil {
				entry["error"] = err.Error()
			} else {
				defer resp.Body.Close()
				var data map[string]any
				if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
					entry["error"] = fmt.Sprintf("HTTP %d 返回非 JSON", resp.StatusCode)
				} else {
					entry["data"] = data
				}
			}
			mu.Lock()
			box[addr] = entry
			mu.Unlock()
		}(u)
	}
	wg.Wait()

	out := make([]map[string]any, 0, len(cfg.urls))
	for _, u := range cfg.urls {
		out = append(out, box[u])
	}
	return out
}

func probeHealth(urls []string) (ok []string, down []string) {
	client := &http.Client{Timeout: probeTimeout}
	var mu sync.Mutex
	var wg sync.WaitGroup
	okSet := make(map[string]bool, len(urls))

	for _, u := range urls {
		wg.Add(1)
		go func(addr string) {
			defer wg.Done()
			good := false
			resp, err := client.Get(addr + "/api/health")
			if err == nil {
				defer resp.Body.Close()
				good = resp.StatusCode < 400
			}
			mu.Lock()
			okSet[addr] = good
			mu.Unlock()
		}(u)
	}
	wg.Wait()

	for _, u := range urls {
		if okSet[u] {
			ok = append(ok, u)
		} else {
			down = append(down, u)
		}
	}
	return ok, down
}

func warnUnhealthy(down []string) {
	if len(down) > healthWarnThreshold {
		fmt.Fprintf(os.Stderr, "警告: 有 %d 个 PanSou 地址失联（超过 %d 个），建议更新 PANSOU_URLS 后再搜\n", len(down), healthWarnThreshold)
		for _, u := range down {
			fmt.Fprintf(os.Stderr, "  - %s\n", u)
		}
	}
}

func printJSON(v any) {
	enc := json.NewEncoder(os.Stdout)
	enc.SetEscapeHTML(false)
	enc.SetIndent("", "  ")
	_ = enc.Encode(v)
}

func verifyToken(cfg serverConfig) map[string]any {
	if len(cfg.urls) != 1 {
		fmt.Fprintln(os.Stderr, "错误: verify / login 仅支持单站点；多站点由 search 自动登录")
		os.Exit(1)
	}
	addr := cfg.urls[0]
	token := loadToken(cfg, addr)
	if token == "" {
		fmt.Println("未找到 token，正在登录...")
		t, err := loginFor(cfg, addr)
		if err != nil {
			fmt.Fprintf(os.Stderr, "请求失败: %v\n", err)
			os.Exit(1)
		}
		return map[string]any{"valid": true, "message": "登录成功", "token": t}
	}

	client := &http.Client{Timeout: timeout}
	req, err := http.NewRequest("POST", addr+"/api/auth/verify", nil)
	if err != nil {
		fmt.Fprintf(os.Stderr, "请求失败: %v\n", err)
		os.Exit(1)
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+token)

	resp, err := client.Do(req)
	if err != nil {
		fmt.Fprintf(os.Stderr, "请求失败: %v\n", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	var data map[string]any
	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		fmt.Fprintf(os.Stderr, "验证响应非 JSON\n")
		os.Exit(1)
	}
	if valid, ok := data["valid"].(bool); ok && valid {
		return data
	}

	fmt.Println("Token 已失效，正在重新登录...")
	_ = os.Remove(tokenFileFor(cfg, addr))
	t, err := loginFor(cfg, addr)
	if err != nil {
		fmt.Fprintf(os.Stderr, "请求失败: %v\n", err)
		os.Exit(1)
	}
	return map[string]any{"valid": true, "message": "已重新登录", "token": t}
}

func runSearch(cfg serverConfig, args []string) {
	if len(args) < 1 {
		fmt.Fprintln(os.Stderr, "用法: pansou search <关键词> [选项]")
		os.Exit(1)
	}

	fs := flag.NewFlagSet("search", flag.ExitOnError)
	channels := fs.String("channels", "", "TG频道，逗号分隔")
	conc := fs.Int("conc", 0, "并发数")
	refresh := fs.Bool("refresh", false, "强制刷新")
	res := fs.String("res", "merge", "返回格式: merge/all/results")
	src := fs.String("src", "all", "数据源: all/tg/plugin")
	plugins := fs.String("plugins", "", "插件，逗号分隔")
	cloudTypes := fs.String("cloud-types", "", "网盘类型，逗号分隔")
	include := fs.String("include", "", "包含关键词，逗号分隔")
	exclude := fs.String("exclude", "", "排除关键词，逗号分隔")
	useGet := fs.Bool("get", false, "使用 GET 方式请求")
	strategy := fs.String("strategy", "first", "多站点策略: first/merge")

	// Go 的 flag 包遇到第一个非 flag 参数就停，把关键词挪到最后再解析
	parseArgs := append(append([]string{}, args[1:]...), args[0])
	if err := fs.Parse(parseArgs); err != nil {
		os.Exit(1)
	}
	if fs.NArg() < 1 {
		fmt.Fprintln(os.Stderr, "用法: pansou search <关键词> [选项]")
		os.Exit(1)
	}
	keyword := fs.Arg(0)

	split := func(s string) []string {
		if s == "" {
			return nil
		}
		parts := strings.Split(s, ",")
		out := make([]string, 0, len(parts))
		for _, p := range parts {
			if p = strings.TrimSpace(p); p != "" {
				out = append(out, p)
			}
		}
		if len(out) == 0 {
			return nil
		}
		return out
	}

	opts := searchOptions{
		channels:   split(*channels),
		conc:       *conc,
		refresh:    *refresh,
		res:        *res,
		src:        *src,
		plugins:    split(*plugins),
		cloudTypes: split(*cloudTypes),
		include:    split(*include),
		exclude:    split(*exclude),
		useGet:     *useGet,
	}

	probeDown := make([]string, 0)
	var probeThread sync.WaitGroup
	if len(cfg.urls) > 1 {
		probeThread.Add(1)
		go func() {
			defer probeThread.Done()
			_, down := probeHealth(cfg.urls)
			probeDown = down
		}()
	}

	result := searchAll(cfg, keyword, opts, *strategy)
	printJSON(result)

	probeThread.Wait()
	warnUnhealthy(probeDown)
}

func main() {
	cfg := loadConfig()
	if len(cfg.urls) == 0 {
		fmt.Fprintln(os.Stderr, "错误: 请设置环境变量 PANSOU_URL 或 PANSOU_URLS")
		os.Exit(1)
	}

	args := os.Args[1:]
	if len(args) == 0 {
		fmt.Println("用法: pansou <command> [options]")
		fmt.Println("命令: health, search, login, verify")
		os.Exit(1)
	}

	switch args[0] {
	case "health":
		result := healthAll(cfg)
		printJSON(result)
		var down []string
		for _, r := range result {
			if r["error"] != nil {
				if u, ok := r["url"].(string); ok {
					down = append(down, u)
				}
			}
		}
		warnUnhealthy(down)

	case "login":
		if len(cfg.urls) != 1 {
			fmt.Fprintln(os.Stderr, "错误: login 仅支持单站点；多站点由 search 自动按需登录")
			os.Exit(1)
		}
		if _, err := loginFor(cfg, cfg.urls[0]); err != nil {
			fmt.Fprintf(os.Stderr, "登录失败: %v\n", err)
			os.Exit(1)
		}
		fmt.Println("登录成功，token 已保存")

	case "verify":
		printJSON(verifyToken(cfg))

	case "search":
		runSearch(cfg, args[1:])

	default:
		fmt.Fprintf(os.Stderr, "未知命令: %s\n", args[0])
		os.Exit(1)
	}
}
