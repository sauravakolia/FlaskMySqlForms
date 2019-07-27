ipt type="text/javascript">
    function yesnoCheck() {
    if (document.getElementById('gstyes').checked) {
        document.getElementById('gstnumber').style.display = 'block';
    }
    else document.getElementById('gstnumber').style.display = 'none';
}

function categ() {
    if(document.getElementById('idelegate').checked)
    {   document.getElementById('indiandelg').style.display = 'block';
        if( document.getElementById('nonmember').checked)
        {
        document.getElementById('membershipNumber').style.display = 'none';

        }
        else{
            document.getElementById('membershipNumber').style.display = 'block';
        }
        document.getElementById('overseasfees').style.display = 'none';
        document.getElementById('sponsorcat').style.display = 'none';
     }   

    else if (document.getElementById('odelegate').checked) {
        document.getElementById('overseasfees').style.display = 'block';
        document.getElementById('membershipNumber').style.display = 'none';
        document.getElementById('sponsorcat').style.display = 'none';
    }

    else if (document.getElementById('sponsor').checked){
        document.getElementById('sponsorcat').style.display = 'block';
        document.getElementById('membershipNumber').style.display = 'none';
        document.getElementById('overseasfees').style.display = 'none';
    }

    else {
        document.getElementById('membershipNumber').style.display = 'none';
        document.getElementById('overseasfees').style.display = 'none';
        document.getElementById('sponsorcat').style.display = 'none';
            }
}

function payment(){
            var pay=0;
        var count=0;
         var returnedArray = [];
        if(document.getElementById("d1_name").value)
            count++;
        if(document.getElementById("d2_name").value)
            count++;
        if(document.getElementById("d3_name").value)
            count++;
        if(document.getElementById("d4_name").value)
            count++;
        if(document.getElementById("d5_name").value)
            count++;
        if(document.getElementById("d6_name").value)
            count++;

        if (document.getElementById('nonmember').checked)
        {
            if(count>=4)
            {   
                pay=10200;
                value1=10200*count; 
                value2=value1+(0.18*value1);
                returnedArray.push(10200);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
                
            }
            else{
                pay=12000;
                value1=12000 *count; 
                value2=value1+(0.18*value1);
                returnedArray.push(12000);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
                }
        }



        if (document.getElementById('corporate').checked)
        {
            if(count>=4)
            {   pay=7650;
                value1=7650 *count; 
                value2=value1+(0.18*value1);
                returnedArray.push(7650);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
            else{
                pay=9000;
                value1=9000  *count; 
                value2=value1+(0.18*value1);
                returnedArray.push(9000);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
        }

        if (document.getElementById('associate').checked)
        {
            if(count>=4)
            {   pay=8400;
                value1=8400 *count; 
                value2=value1+(0.18*value1);
                returnedArray.push(8400);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
            else{
                pay=10200;
                value1=10200  *count; 
                value2=value1+(0.18*value1);
                returnedArray.push(10200);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
        }

        if (document.getElementById('odelegate').checked)
        {
            if(count>=4)
            {   
                pay=595*70;
                value1=((595*70)*count); 
                value2=value1+(0.18*value1);
                returnedArray.push(pay);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
            else{
                pay=700*70;
                value1=((700*70)*count); 
                value2=value1+(0.18*value1);
                returnedArray.push(pay);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
        }

         if (document.getElementById('sponsorcat').checked)
        {
            if(document.getElementById('sponsorcat')=="nonmember")
            {   pay=10000;
                value1=10000*count; 
                value2=value1+(0.18*value1);
                returnedArray.push(10000);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
            else{
                count=12000;
                value1=12000*count ; 
                value2=value1+(0.18*value1);
                returnedArray.push(12000);
                returnedArray.push(count);
                returnedArray.push(value1);
                returnedArray.push(value2);
            }
        }
             
        return returnedArray;
    }

function gstamount(){
        var myarry=payment();
         document.getElementById("amountdgst").value=myarry[3]; 
       }

       function amount(){
        var amountarray=payment();
        document.getElementById("amountd").value=amountarray[2];
       }

       function paymentbrk(){
        var payarray=payment();
        document.getElementById("paymentbreakup").innerHTML="Payment of "+payarray[1]+ "Delegate=" +payarray[0]+ "*" +payarray[1]+ "="+ payarray[2]+
        " \n Sum of Total Amount: Rs." +payarray[0]+'\n'+"Total Amount to be Paid (18% GST): Rs."+ payarray[3]+"/-";

       }
    