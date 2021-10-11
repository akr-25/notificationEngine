const express = require('express');
const cors = require('cors');
const morgan = require('morgan')

app = express();
app.use(cors());
app.use(morgan("common"));

app.get("/api/test", (req, res) => {
    return res.status(200).send({
        "employee": "Abhishek",
        "email": "abhishek@abc.com",
        "transactions": "3"
    });
})

app.listen(3030, () => {
    console.log("Listening on port 3030");
})