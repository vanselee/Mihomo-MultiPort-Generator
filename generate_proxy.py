import urllib.request
import yaml
import sys

def generate_mihomo_config(sub_url, output_file="mihomo_multi_port.yaml"):
    print(f"[*] 正在获取订阅链接...\nURL: {sub_url}")
    
    req = urllib.request.Request(
        sub_url, 
        headers={'User-Agent': 'ClashforWindows/0.19.23'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8')
    except Exception as e:
        print(f"[!] 下载订阅失败: {e}")
        return

    try:
        data = yaml.safe_load(content)
        if not data or 'proxies' not in data:
            raise ValueError("未找到 proxies 节点数据")
    except Exception as e:
        print("[!] 订阅解析失败！")
        return

    proxies = data.get('proxies', [])
    if not proxies:
        print("[!] 订阅解析成功，但没有发现任何节点。")
        return

    max_nodes = 50
    selected_proxies = proxies[:max_nodes]
    
    print(f"[*] 共获取到 {len(proxies)} 个节点，选取前 {len(selected_proxies)} 个分配多端口...")

    listeners = []
    rules = []
    start_port = 10001

    for i, proxy in enumerate(selected_proxies):
        proxy['skip-cert-verify'] = True
        
        port = start_port + i
        node_name = f"[{port}] {proxy['name']}"
        proxy['name'] = node_name
        
        listeners.append({
            'name': f"inbound-{port}",
            'type': 'mixed',
            'port': port
        })
        
        rules.append(f"IN-PORT,{port},{node_name}")

    rules.append("MATCH,DIRECT")

    mihomo_config = {
        'allow-lan': True,
        'mode': 'rule',
        'log-level': 'info',
        'proxies': selected_proxies,
        'listeners': listeners,
        'rules': rules
    }

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(mihomo_config, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"\n[+] 配置文件已成功生成: {output_file}")
    except Exception as e:
        print(f"[!] 写入文件失败: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("请输入你的 Clash 订阅链接: ").strip()
    
    if url:
        generate_mihomo_config(url)
