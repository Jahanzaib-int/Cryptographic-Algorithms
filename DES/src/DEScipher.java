import javax.crypto.*;
import javax.swing.*;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;


public class DEScipher {



    public static void main(String[] args) throws NoSuchAlgorithmException, BadPaddingException, IllegalBlockSizeException, NoSuchPaddingException, InvalidKeyException {
         String Message;
        KeyGenerator MykeyGenerator = KeyGenerator.getInstance("DES");
        SecretKey MyDEESkey= MykeyGenerator.generateKey();

        Cipher encrypt =Cipher.getInstance("DES");

        encrypt.init(Cipher.ENCRYPT_MODE,MyDEESkey);
        Message =JOptionPane.showInputDialog(null,"Enter message to encrypt");
        byte[] mybyte =Message.getBytes();

        byte[] myencryptedbyte = encrypt.doFinal(mybyte);
        JOptionPane.showMessageDialog(null,"Encrypted Data "+"\n"+myencryptedbyte);

        System.out.println("Encrypted message is "+ Arrays.toString(myencryptedbyte));

        Cipher dencrypt =Cipher.getInstance("DES");




        dencrypt.init(Cipher.DECRYPT_MODE,MyDEESkey);
        byte[] Dmyencryptedbyte =  dencrypt.doFinal(myencryptedbyte);

        String actual_msg =  new String(Dmyencryptedbyte);

        System.out.println("Decrypted Cipher is " +actual_msg);

    }
}
