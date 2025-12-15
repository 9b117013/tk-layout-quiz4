# Tkinter 佈局練習 - 第4次小考

專案包含三個 Python 程式，分別使用 Tkinter 的三種佈局方式（Pack、Grid、Place）實作相同外觀的視窗介面。

** 包含加分題：RWD 自適應佈局 **

## 專案結構

```
tk-layout-quiz4/
├── tk_pack.py        # 使用 Pack 佈局（支援 RWD）
├── tk_grid.py        # 使用 Grid 佈局（支援 RWD）
├── tk_place.py       # 使用 Place 佈局（支援 RWD）
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md
```

## 視窗規格

- **視窗大小**：400x300 像素（初始）
- **視窗可調整**：`resizable(True, True)` - 支援 RWD
- **視窗標題**：
  - `tk_pack.py` → "Tkinter Pack"
  - `tk_grid.py` → "Tkinter Grid"
  - `tk_place.py` → "Tkinter Place"

## 佈局結構

視窗包含 5 個 Frame 區塊：

| 區塊 | 顏色 | 尺寸 |
|------|------|------|
| 左側欄 | lightgreen | 寬度 40px (10%) |
| 右側欄 | lightblue | 寬度 40px (10%) |
| 上層 | red | 高度 60px (20%) |
| 中層 | yellow | 填滿剩餘空間 (70%) |
| 下層 | blue | 高度 30px (10%) |

紅色區塊內包含 3 個 Label（白底黑字，靠上對齊）：
- left
- center
- Right

## 執行方式

使用 Python 3.x 執行任一程式：

```bash
python tk_pack.py
python tk_grid.py
python tk_place.py
```

## 環境需求

- Python 3.x
- Tkinter（Python 內建，無需額外安裝）

## 佈局說明

### Pack 佈局
- 使用 `side` 參數控制元件排列方向
- 先切左右側欄，再切上中下區域
- 使用 `pack_propagate(False)` 維持固定尺寸
- **RWD**：黃色區域使用 `fill="both", expand=True` 自動延展

### Grid 佈局
- 使用 3x3 的網格結構
- 左右側欄使用 `rowspan=3` 跨越所有列
- 使用 `columnconfigure` 和 `rowconfigure` 設定權重
- **RWD**：中間欄列設定 `weight=1` 自動延展

### Place 佈局
- 使用相對座標 `relx`、`rely` 定位
- 使用 `relwidth`、`relheight` 設定相對大小
- **RWD**：所有區塊使用相對定位，依百分比縮放

## 加分題：RWD 自適應佈局

專案實作了 RWD 自適應佈局：

| 佈局 | RWD 行為 |
|------|----------|
| Pack | 黃色區域自動填滿，左右欄與紅藍條維持固定大小 |
| Grid | 黃色區域自動填滿，周圍色塊維持固定大小 |
| Place | 所有色塊依照百分比縮放 |


