# MD2Card 推文模板

这是我们当前**微信（公众号）和小红书**推文的制作 pipeline：

```
Markdown 文案 ──┐
                ├──► md2card 渲染 ──► 推文卡片图
自定义 CSS ─────┘
```

使用 [md2card](https://md2card.com) 将 Markdown 文案结合自定义 CSS 渲染成卡片样式的推文图，再发布到微信/小红书。

## 文件说明

| 文件 | 说明 |
| --- | --- |
| `robotics_md_template.css` | 当前模板样式：卡片整体（页首队徽 Logo、标题层级、正文、列表、引用、图片、分割线、CTA 按钮）及小屏幕适配 |
| `robotics_card_wechat_url_logo.css` | 微信公众号版本：Logo 以 data URL 内嵌的单文件版，不依赖外部图片，便于直接粘贴到公众号后台 |

## 使用流程

1. 撰写推文文案（Markdown）
2. 选择对应平台的 CSS（公众号用 wechat 版，小红书用模板版）
3. 用 md2card 以选定的 CSS 渲染 Markdown，导出卡片图
4. 发布到微信/小红书

## 注意事项

- 模板中引用的图片（队徽、队标、公众号二维码）位于仓库 `logos/` 目录；使用 GitHub raw 链接时，大陆网络环境下加载可能缓慢或不稳定，建议在香港等稳定网络环境下操作。
- 发布前请确认公众号二维码仍是当前有效版本（`logos/team-wechat-qrcode-258.png`）。
