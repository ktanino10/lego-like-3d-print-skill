# lego-like-3d-print-skill

**個人の趣味・学習を目的とした非公式の制作支援スキルです。各社の公式提供・推奨や、互換性・造形結果の保証を示すものではありません。**

[English](README.en.md) · [日本語サイト](https://ktanino10.github.io/lego-like-3d-print-skill/ja/) · [English site](https://ktanino10.github.io/lego-like-3d-print-skill/en/)

8 mmピッチのブロック風模型を、実際に分割・組立できる部品として考えるためのGitHub Copilot用スキルです。
FreeCADによる実CADから、印刷資料、Blender完成CG・組立動画、対話3Dガイド、承認されたGitHub Pages公開まで、
**同じ形状・配置・部品IDをつなぐ制作手順**を提供します。

**趣旨と許可は別です。** 新規スキル本文・文書・スクリプトは[MIT](LICENSE)で、
商用利用も認めます。「趣味・学習向け」は利用目的の説明で、個人利用限定・非商用限定ではありません。
外部作品、写真、ロゴ、商標、フォント、FreeCAD・Blender本体の権利は再許諾しません。
[権利と注意事項](NOTICES.md)を確認してください。

## 最短の入口

1. **[導入ガイド](docs/ja/install.md)** — スキルの安全なコピー、FreeCAD・BlenderのmacOS / Windows / Linux導入、最初の小さな確認。
2. **[使い方と依頼例](docs/ja/usage.md)** — 何をAIへ頼み、どの成果物を受け取り、どこで実物確認するか。
3. **[実際の作例と確認範囲](docs/ja/examples.md)** — 公開2作品の紹介。CG・設計・実物報告を区別。

[スキルだけのZIP](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip)
またはこのrepoの **Code → Download ZIP** を保存し、展開して内容を確認します。
[配布フォルダー](.github/skills/lego-like-3d-print/)全体を、
`~/.copilot/skills/lego-like-3d-print`（個人用）か
自分のrepoの`.github/skills/lego-like-3d-print`（プロジェクト用）の**どちらか**へコピーします。
既存スキルへ上書きしない手順は[導入ガイド](docs/ja/install.md#skill-install)にあります。

CLIでは新しいセッションを開始するか、実行中なら`/skills reload`の後に
`/skills info lego-like-3d-print`で確認します。Copilot appではコピー後に対象プロジェクトの新しいセッションを開きます。
CLIコマンドがappにもあるとは仮定しません。

```text
lego-like-3d-printを使って、猫を8 mmピッチのブロック風卓上模型にして。
まず1案と少量の嵌合試験・代表部品まで。保存先はこのプロジェクト。
実CADと同じ形状のCG・組立手順を用意し、公開と本番全数印刷はまだしないで。
```

## 含むもの・含まないもの

| 含む | 含まない |
| --- | --- |
| 1つの`SKILL.md`、日英の寸法基準・制作手順、MIT/notice | 完成模型一式の生成器、CADモデル、元作品の画像・写真 |
| 日英導入・使い方・作例・注意事項、静的サイト | FreeCAD / Blender本体、フォント、MCPの自動導入・常駐 |
| 別の一時フォルダーへ小箱を作るtest-only smoke scripts | スライス済み印刷ファイル、プリンター設定、Send/Print処理 |

読むだけ・公開3Dを見るだけならCADアプリは不要です。実CAD生成にはFreeCAD、
実メッシュのCG/動画にはBlenderと、それを実行できるshellまたは対応ツール接続が必要です。
スキルは日本語・英語の依頼を認識し、依頼者の言語で応答します。
既定は1作品1案。サイズ変更はブロック数・配置で行い、完成STL全体を拡大縮小しません。

## 基準と実物の境界

基準は8.0 mmピッチ、本体9.6 mm、プレート3.2 mm、スタッド径4.8 mm・高さ1.8 mm、
本体全体差0.2 mm、メス**半径方向**クリアランス+0.04 mmです。
[自己完結した基準資料](.github/skills/lego-like-3d-print/references/baseline.ja.md)を参照してください。

主参照Bは191.8×80.2×238.6 mm / 150部品 / 28工程ですが、新作の固定目標ではありません。
2026-09-23の実物報告は**Bの台座・前面まで**。顔を含む全数、保持力・強度・転倒の測定合格は未確認です。
形状3MFは**NOT_SLICED**で、設定済みP1Sプロジェクトではありません。

[公開サイト](https://ktanino10.github.io/lego-like-3d-print-skill/ja/) ·
[注意事項](docs/ja/notices.md) ·
[サイトの再生成・検証](CONTRIBUTING.md)
