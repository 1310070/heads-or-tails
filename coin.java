import java.util.Scanner;

class ren{



public static void main(String[] args){



Scanner sc=new Scanner(System.in);



System.out.println("コイントス回数入力");

int c=sc.nextInt();

int ue=0;

int sita=0;

for(int i=0;i<c;i++){

int d=(int)(Math.random()*2);

if(d==1){

ue++;

}else if(d==0){

sita++;

}





}

System.out.print("表:"+ue);

System.out.print("裏:"+sita);



}







}
