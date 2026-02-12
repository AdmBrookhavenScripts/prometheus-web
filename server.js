const express = require("express");
const multer = require("multer");
const { exec } = require("child_process");
const fs = require("fs");

const app = express();
const upload = multer({ dest: "uploads/" });

app.use(express.static("public"));

app.post("/upload", upload.single("file"), (req, res) => {
    if (!req.file) return res.status(400).send("Nenhum arquivo enviado");

    if (!req.file.originalname.endsWith(".lua"))
        return res.status(400).send("Apenas arquivos .lua");

    const input = req.file.path;

    const cmd = `luajit Prometheus/cli.lua --preset Medium --nocolors ${input}`;

    exec(cmd, (err) => {
        if (err) {
            console.error(err);
            return res.status(500).send("Erro ao obfuscar");
        }

        const output = input + ".obfuscated.lua";

        res.download(output, "obfuscated.lua", () => {
            fs.unlinkSync(input);
            fs.unlinkSync(output);
        });
    });
});

app.listen(3000, () => console.log("🔥 Servidor rodando"));
