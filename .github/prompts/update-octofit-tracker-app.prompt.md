mode: 'agent'
model: GPT-4.1

# Django アプリの更新

- すべての Django プロジェクトファイルは `octofit-tracker/backend/octofit_tracker` ディレクトリにあります。

1. MongoDB 接続と CORS を有効にするために `settings.py` を更新します。
2. ユーザー、チーム、アクティビティ、リーダーボード、ワークアウトのコレクションをサポートするために `models.py`、`serializers.py`、`urls.py`、`views.py`、`tests.py`、`admin.py` を更新します。
3. `/` が API を指していること、および `urls.py` に `api_root` が存在することを確認します。
