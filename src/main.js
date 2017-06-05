import answer from 'the-answer'

import KarmaBot from './KarmaBot'
import UrlVerification from './UrlVerification'


const express = require('express')
const bodyParser = require('body-parser')

const app = express()
const karmaBot = new KarmaBot()
const urlVerification = new UrlVerification()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

app.get('/', (req, res) => {
  res.send(`the answer is ${answer}.`)
})

app.post('/slack',(req, res) => {
    const params = Object.assign({},req.body)
    urlVerification.process(req, res)
    karmaBot.process(params)
})

app.listen(5000, function () {
  console.log('Example app listening on port 5000!')
})