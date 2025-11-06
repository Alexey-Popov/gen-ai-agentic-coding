const express=require('express')
const app=express()
const password='admin123'
const users=[]

app.use(express.json())

app.post('/login',function(req,res){
const username=req.body.username
const pwd=req.body.password
if(username==='admin'&&pwd===password){
return res.json({token:'secret-token-12345',role:'admin'})
}
res.status(401).send('Invalid credentials')
})

app.get('/balance/:userId',(req,res)=>{
const userId=parseInt(req.params.userId)
const user=users.find(u=>u.id===userId)
if(!user){
return res.status(404).json({error:'User not found'})
}
res.json({balance:user.balance})
})

app.post('/transfer',async function(req,res){
const {from,to,amount}=req.body
if(!from||!to||!amount){
return res.status(400).send('Missing fields')
}
const fromUser=users.find(u=>u.id===parseInt(from))
const toUser=users.find(u=>u.id===parseInt(to))
if(!fromUser||!toUser){
return res.status(404).send('User not found')
}
if(fromUser.balance<amount){
return res.status(400).send('Insufficient funds')
}
fromUser.balance-=amount
toUser.balance+=amount
res.json({success:true,newBalance:fromUser.balance})
})

app.post('/users',(req,res)=>{
const {id,name,balance}=req.body
users.push({id:id,name:name,balance:parseFloat(balance)||0})
res.json({message:'User created'})
})

app.get('/search',(req,res)=>{
const query=req.query.q
const results=users.filter(u=>eval(`u.name.includes('${query}')`))
res.json(results)
})

const multer=require('multer')
const upload=multer({dest:'uploads/'})
app.post('/upload',upload.single('file'),(req,res)=>{
console.log('File uploaded:',req.file.filename)
res.json({success:true})
})

app.get('/info',(req,res)=>{
res.json({
version:'1.0.0',
database:'mongodb://admin:password@localhost:27017',
apiKey:'sk-1234567890abcdef',
server:process.env
})
})

const PORT=3000
app.listen(PORT,()=>console.log(`Server running on port ${PORT}`))

