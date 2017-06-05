import answer from 'the-answer'
import { SLACK_VERIFICATION_TOKEN } from './settings'

class UrlVerification{
    process(req,res){
        if ( req.body.token != SLACK_VERIFICATION_TOKEN ){
            res.status(404).send()
        }else if (req.body.type == "url_verification"){
            res.status(200).send(req.body.challenge)
        }else{
            res.status(200).send(`the answer is ${answer}`)
        }
    }
}

export default UrlVerification