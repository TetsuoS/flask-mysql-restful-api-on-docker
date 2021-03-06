<h2>Local:</h2>

t-saito@MacBookPronoMacBook-Pro flask-mysql-restful-api-on-docker]$ pwd
/Users/t-saito/flask-mysql-restful-api-on-docker


<h2>エラー</h2>
root@458c0a7e00a3:/src# flask db migrate
ERROR [root] Error: cryptography is required for sha256_password or caching_sha2_password

エラーの解決方法

エラーが発生する原因はPythonの暗号化ライブラリ不足。
つまり以下のコマンドで暗号化ライブラリを追加すれば解決する。

pip install cryptography
参考
Improve helpfulness of error message when cryptography is required · Issue #768 · PyMySQL/PyMySQL · GitHub






<h2>参照</h2>
PythonのFlaskでMySQLを利用したRESTfulなAPIをDocker環境で実装する


# flask-mysql-restful-on-docker

PythonのFlaskでMySQLを利用したRESTfulなAPIをDocker環境で実装する  
https://qiita.com/kai_kou/items/5d73de21818d1d582f00

## Install

```sh
> git clone https://github.com/kai-kou/flask-mysql-restful-api-on-docker.git
> cd flask-mysql-restful-api-on-docker
> docker-compose up -d
> docker-compose exec api bash
>> flask db upgrade
```

## Usage

```sh
# POST
> curl -X POST http://localhost:5000/hoges \
  -H "Content-Type:application/json" \
  -d "{\"name\":\"hoge\",\"state\":\"hoge\"}"

# PUT
> curl -X PUT http://localhost:5000/hoges/[id] \
  -H "Content-Type:application/json" \
  -d "{\"name\":\"hogehoge\"}"

# GET
> curl http://localhost:5000/hoges/[id]

# GET List
> curl http://localhost:5000/hoges

# DELETE
> curl -X DELETE http://localhost:5000/hoges/[id]
```
