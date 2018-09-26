import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;


public class DES {

    public static void main(String[] args) throws Exception
    {
        KeyGenerator Keygen= KeyGenerator.getInstance("DES");
        SecretKey DESKey = Keygen.generateKey();

        Cipher descipher =Cipher.getInstance("DES");

        descipher.init(Cipher.ENCRYPT_MODE,DESKey);

        byte[] mybyte ="how are you".getBytes();

        byte[] myencryptedbyte = descipher.doFinal(mybyte);

        System.out.println(myencryptedbyte);

    }
}
