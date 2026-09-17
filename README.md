# Mihomo Multi-Port Config Generator

[🇨🇳 中文文档请往下看](#-中文说明)

A lightweight Python script that converts standard Clash subscription links into **Mihomo (Clash Meta)** Multi-Port Inbounds configuration files.

## ✨ Core Features & Use Cases

**Core Problem Solved: One-machine multi-node isolation (Assigning different browser profiles to different proxy nodes).**

When managing multiple social media or e-commerce accounts on a single computer, it's often necessary to assign a different IP address (country or region) to each browser profile to prevent account association.

This script automates the process:
1. **Auto-Parses** your Clash subscription link.
2. **Multi-Port Allocation**: Automatically allocates independent local listening ports for each node (starting from `10001` by default).
3. **Node Renaming**: Automatically adds a port number prefix to the node name (e.g., `[10001] Node A`) for easy identification in your proxy client.
4. **Force Skip Certificate Verification**: Automatically forces `skip-cert-verify: true` for all nodes, fixing connection drops caused by strict certificate issues on some nodes.
5. Generates a clean, bloat-free `mihomo_multi_port.yaml` file.

## 🚀 Installation

Ensure you have Python 3 installed. Then, install the required `PyYAML` library:

```bash
pip install pyyaml
```

## 🛠️ Usage

### Method 1: Command-line Argument
Pass your Clash subscription link directly via the command line:
```bash
python generate_proxy.py "http://your-subscription-link..."
```

### Method 2: Interactive Mode
Run the script without arguments and it will prompt you for the link:
```bash
python generate_proxy.py
```

Upon success, a `mihomo_multi_port.yaml` file will be generated in the same directory.

## 💻 How to use in clients?

### 1. Start the Proxy Core (Clash Verge / Mihomo)
- Drag and drop the generated `mihomo_multi_port.yaml` into your **Clash Verge** "Profiles" list.
- Click to select and activate the profile.
- **⚠️ IMPORTANT**: Turn off **System Proxy** and **TUN Mode** in the settings. Ensure the Proxy Mode is set to **Rule**.

### 2. Browser Traffic Split Setup
In the browser you want to isolate (e.g., Chrome):
- Create a new Browser Profile (Profile 1), install and open the `Proxy SwitchyOmega` extension.
- Set Proxy Protocol to `SOCKS5` (or `HTTP`).
- Set Proxy Server to `127.0.0.1` and Port to `10001`.
- Create another Browser Profile (Profile 2), repeat the setup, but set Port to `10002`.
- And so on...

Your Profile 1 traffic will strictly route through Node 1, Profile 2 through Node 2, perfectly achieving physical-level IP isolation.

## 📝 Notes
- The script defaults to extracting the first 50 nodes (port range `10001` - `10050`). You can manually change the `max_nodes` parameter inside the script if you need more.
- This script only supports standard **Clash YAML format** subscriptions (provided by most proxy providers). It does not support parsing raw Base64 vmess/vless links directly.

---

<h2 id="-中文说明">🇨🇳 中文说明</h2>

这是一个用 Python 编写的轻量级脚本，用于将标准的 Clash 订阅链接转换为 **Mihomo (Clash Meta)** 的多端口入站 (Multi-Port Inbounds) 配置文件。

## ✨ 核心功能与使用场景

**核心解决的问题：一机多节点隔离（一个浏览器 Profile 对应一个代理节点）。**

很多时候我们需要在同一台电脑上管理多个社交媒体或电商账号（例如跨境电商运营）。为了防止账号关联，每个浏览器的配置文件（Profile）需要分配到不同的国家或地区 IP。

本脚本可以自动化完成这一过程：
1. **自动解析**你提供的 Clash 订阅链接。
2. **多端口分配**：为每个节点自动分配独立的本地监听端口（默认从 `10001` 开始）。
3. **节点重命名**：自动在节点名称前添加端口号前缀（如 `[10001] 节点A`），方便在客户端中直观辨认。
4. **强制解除证书验证**：自动为所有节点强制开启 `skip-cert-verify: true`，解决部分节点因为证书问题断流的现象。
5. 生成纯净、无冗余的 `mihomo_multi_port.yaml` 文件。

## 🚀 安装依赖

运行本脚本前，确保你的电脑已安装 Python 3 环境。然后安装必要的依赖库 `PyYAML`：

```bash
pip install pyyaml
```

## 🛠️ 使用方法

### 方式 1：命令行参数直接运行
在终端中直接通过参数传入你的 Clash 订阅链接：
```bash
python generate_proxy.py "http://你的订阅链接..."
```

### 方式 2：交互式运行
直接运行脚本，脚本会提示你输入订阅链接：
```bash
python generate_proxy.py
```

执行成功后，会在同级目录下生成一个 `mihomo_multi_port.yaml` 文件。

## 💻 客户端如何使用？

### 1. 启动代理核心 (Clash Verge / Mihomo)
- 将生成的 `mihomo_multi_port.yaml` 拖入 **Clash Verge** 的“配置 (Profiles)”列表中。
- 单击选中该配置以激活。
- **⚠️ 重要提醒**：请在设置中 **关闭系统代理 (System Proxy)** 和 **关闭 TUN 模式**。代理模式选为 **规则 (Rule)** 即可。

### 2. 浏览器分流设置
在你想进行隔离的浏览器中（例如 Chrome）：
- 新建浏览器 Profile 1，安装并打开 `Proxy SwitchyOmega` 插件。
- 代理协议选择 `SOCKS5` (或 `HTTP`)。
- 代理服务器填写 `127.0.0.1`，端口填写 `10001`。
- 新建浏览器 Profile 2，进行同样的操作，代理端口填写 `10002`。
- 依次类推...

这样，你的 Profile 1 流量会固定走节点 1，Profile 2 会固定走节点 2，完美实现物理环境级别的 IP 隔离。

## 📝 注意事项
- 本脚本默认截取订阅前 50 个节点（端口范围 `10001` - `10050`），如果你有特殊需求，可以直接修改脚本里的 `max_nodes` 参数。
- 本脚本仅支持解析标准的 **Clash YAML 格式** 订阅（大部分机场均默认提供此格式）。不支持直接解析 Base64 的原始 vmess/vless 链接。
